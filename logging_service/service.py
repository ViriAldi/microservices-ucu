from flask import Flask, request
import hazelcast
import consul
import os

SERVICE_NAME = os.getenv("SERVICE_NAME")
SERVICE_PORT = os.getenv("FLASK_RUN_PORT")
SERVICE_HOST = os.getenv("SERVICE_HOST")

CONSUL_HOST = os.getenv("CONSUL_HOST")
CONSUL_PORT = os.getenv("CONSUL_PORT")

cs = consul.Consul(host=CONSUL_HOST, port=CONSUL_PORT)
cs.agent.service.register(
    name=SERVICE_NAME,
    port=SERVICE_PORT,
    address=SERVICE_HOST,
    service_id=f"{SERVICE_NAME}:{SERVICE_PORT}",
)

HAZELCAST_MAP = cs.kv.get("hc_map")[1]["Value"].decode("utf-8")


app = Flask(__name__)
client = hazelcast.HazelcastClient()
messages_storage = client.get_map(HAZELCAST_MAP).blocking()
messages_storage.clear()


@app.post("/")
def handle_post():
    uid = request.get_json()["UUID"]
    msg = request.get_json()["msg"]

    messages_storage.lock(uid)
    messages_storage.put(uid, msg)
    messages_storage.unlock(uid)

    app.logger.info(f"Received {msg}")
    return "", 200


@app.get("/")
def handle_get():
    response_body = {
        "concat_msgs": " ".join(messages_storage.values()),
    }
    return response_body, 200


if __name__ == "__main__":
    app.run()
