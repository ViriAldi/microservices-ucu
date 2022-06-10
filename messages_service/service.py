from flask import Flask
import logging

HTTP_HOST = "http://127.0.0.1"
FACADE_PORT = 8000
MESSAGES_PORT = 8002
FACADE_URL = f"{HTTP_HOST}:{FACADE_PORT}"

logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.get("/")
def handle_get():
    response_body = {
        "msg": "static",
    }
    return response_body, 200


if __name__ == "__main__":
    logging.info("Messages service has started")
    app.run(debug=True)
