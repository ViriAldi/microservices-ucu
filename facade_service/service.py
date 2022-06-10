from flask import Flask, request
import requests
import random
import uuid

HTTP_HOST = "http://127.0.0.1"
LOGGING_PORT_LIST = [8001, 8002, 8003]
MESSAGES_PORT = 8004

LOGGING_URLS = [f"{HTTP_HOST}:{PORT}" for PORT in LOGGING_PORT_LIST]
MESSAGES_URL = f"{HTTP_HOST}:{MESSAGES_PORT}"

app = Flask(__name__)


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

    return "", logging_response.status_code


@app.get("/facade_service")
def handle_get():
    logging_url = random.choice(LOGGING_URLS)
    logging_response = requests.get(logging_url).json()["concat_msgs"]
    messages_response = requests.get(MESSAGES_URL).json()["msg"]

    response = " ".join([logging_response, messages_response])
    return response


if __name__ == "__main__":
    app.logger.info("Facade service has started")
    app.run()
