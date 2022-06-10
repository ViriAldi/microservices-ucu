from flask import Flask, request
import hazelcast
import requests
import random
import uuid

HTTP_HOST = "http://127.0.0.1"
LOGGING_PORT_LIST = [8001, 8002, 8003]
MESSAGES_PORTS = [8004, 8005]

LOGGING_URLS = [f"{HTTP_HOST}:{PORT}" for PORT in LOGGING_PORT_LIST]
MESSAGES_URLs = [f"{HTTP_HOST}:{PORT}" for PORT in MESSAGES_PORTS]

app = Flask(__name__)
client = hazelcast.HazelcastClient()
msg_queue = client.get_queue("messages-queue").blocking()
msg_queue.clear()


@app.post("/facade_service")
def handle_post():
    uid = str(uuid.uuid4())
    msg = request.get_json()["msg"]

    logging_body = {
        "UUID": uid,
        "msg": msg,
    }

    logging_url = random.choice(LOGGING_URLS)
    logging_response = requests.post(logging_url, json=logging_body)

    msg_queue.put(msg)

    return "", logging_response.status_code


@app.get("/facade_service")
def handle_get():
    logging_url = random.choice(LOGGING_URLS)
    logging_response = requests.get(logging_url).json()["concat_msgs"]

    messages_url = random.choice(MESSAGES_URLs)
    messages_response = requests.get(messages_url).json()["concat_msgs"]

    response = " ".join([logging_response, messages_response])
    return response


if __name__ == "__main__":
    app.logger.info("Facade service has started")
    app.run()
