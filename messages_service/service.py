from flask import Flask
from threading import Thread
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

HAZELCAST_MQ = cs.kv.get("hc_queue")[1]["Value"].decode("utf-8")


app = Flask(__name__)
client = hazelcast.HazelcastClient()
msg_queue = client.get_queue(HAZELCAST_MQ).blocking()
msg_queue.clear()
messages_storage = []


@app.get("/")
def handle_get():
    response_body = {
        "concat_msgs": " ".join(messages_storage),
    }
    return response_body, 200


if __name__ == "__main__":
    def consume_messages():
        while True:
            val = msg_queue.take()
            app.logger.info(f"Consumed {val}")
            messages_storage.append(val)


    thr = Thread(target=consume_messages)
    thr.start()
    app.run()
