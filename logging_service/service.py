from flask import Flask, request
import hazelcast


app = Flask(__name__)
client = hazelcast.HazelcastClient()
messages_storage = client.get_map("logging-map").blocking()
messages_storage.clear()


@app.post("/")
def handle_post():
    uid = request.get_json()["UUID"]
    msg = request.get_json()["msg"]

    messages_storage.lock(uid)
    messages_storage.put(uid, msg)
    messages_storage.unlock(uid)

    app.logger.info(f"{msg}")
    return "", 200


@app.get("/")
def handle_get():
    response_body = {
        "concat_msgs": " ".join(messages_storage.values()),
    }
    return response_body, 200


if __name__ == "__main__":
    app.run()
