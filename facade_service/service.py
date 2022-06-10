from flask import Flask, request
import logging
import requests
import uuid

HTTP_HOST = "http://127.0.0.1"
FACADE_PORT = 8000
LOGGING_PORT = 8001
MESSAGES_PORT = 8002

LOGGING_URL = f"{HTTP_HOST}:{LOGGING_PORT}"
MESSAGES_URL = f"{HTTP_HOST}:{MESSAGES_PORT}"

# logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.post("/facade_service")
def handle_post():
    uid = str(uuid.uuid4())
    msg = request.get_json()["msg"]

    logging_body = {
        "UUID": uid,
        "msg": msg,
    }
    logging_response = requests.post(LOGGING_URL, json=logging_body)

    return {}, logging_response.status_code


@app.get("/facade_service")
def handle_get():
    logging_response = requests.get(LOGGING_URL).json()["concat_msgs"]
    messages_response = requests.get(MESSAGES_URL).json()["msg"]

    response_body = {
        "concat_msgs": " ".join([logging_response, messages_response]),
    }

    return response_body, 200


if __name__ == "__main__":
    app.logger.info("Facade service has started")
    app.run(debug=True)
