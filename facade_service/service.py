from flask import Flask, request
import hazelcast
import requests
import consul
import random
import uuid
import os

HTTP = "http://"

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

logging_services = filter(lambda x: x["Service"] == "logging-service", cs.agent.services().values())
messages_services = filter(lambda x: x["Service"] == "messages-service", cs.agent.services().values())
LOGGING_URLS = [f'{HTTP}{item["Address"]}:{item["Port"]}' for item in logging_services]
MESSAGES_URLS = [f'{HTTP}{item["Address"]}:{item["Port"]}' for item in messages_services]

HAZELCAST_MQ = cs.kv.get("hc_queue")[1]["Value"].decode("utf-8")


app = Flask(__name__)
client = hazelcast.HazelcastClient()
msg_queue = client.get_queue(HAZELCAST_MQ).blocking()
msg_queue.clear()


@app.post("/facade_service")
def handle_post():
    uid = str(uuid.uuid4())
    msg = request.get_json()["msg"]

    logging_body = {
        "UUID": uid,
        "msg": msg,
    }
    print(LOGGING_URLS)
    logging_url = random.choice(LOGGING_URLS)
    logging_response = requests.post(logging_url, json=logging_body)

    msg_queue.put(msg)

    return "", logging_response.status_code


@app.get("/facade_service")
def handle_get():
    logging_url = random.choice(LOGGING_URLS)
    logging_response = requests.get(logging_url).json()["concat_msgs"]

    messages_url = random.choice(MESSAGES_URLS)
    messages_response = requests.get(messages_url).json()["concat_msgs"]

    response = " ".join([logging_response, messages_response])
    return response


if __name__ == "__main__":
    app.logger.info("Facade service has started")
    app.run()
