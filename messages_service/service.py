from flask import Flask


app = Flask(__name__)


@app.get("/")
def handle_get():
    response_body = {
        "msg": "static",
    }
    return response_body, 200


if __name__ == "__main__":
    app.run()
