from flask import Flask, request
import logging

HTTP_HOST = "http://127.0.0.1"
FACADE_PORT = 8000
LOGGING_PORT = 8001
FACADE_URL = f"{HTTP_HOST}:{FACADE_PORT}"

logger = logging.getLogger(__name__)
app = Flask(__name__)

messages_storage = {}


@app.post("/")
def handle_post():
    uid = request.get_json()["UUID"]
    msg = request.get_json()["msg"]

    messages_storage[uid] = msg
    app.logger.info(f"{msg}")

    return "", 200


@app.get("/")
def handle_get():
    response_body = {
        "concat_msgs": " ".join(messages_storage.values()),
    }
    return response_body, 200


if __name__ == "__main__":
    logging.info("Logging service has started")
    app.run(debug=True)
