from flask import Flask
from threading import Thread
import hazelcast

app = Flask(__name__)
client = hazelcast.HazelcastClient()
msg_queue = client.get_queue("messages-queue").blocking()
msg_queue.clear()

messages_storage = []


def consume_messages():
    while True:
        val = msg_queue.take()
        app.logger.info(f"Consumed {val}")
        messages_storage.append(val)


thr = Thread(target=consume_messages)
thr.start()


@app.get("/")
def handle_get():
    response_body = {
        "concat_msgs": " ".join(messages_storage),
    }
    return response_body, 200


if __name__ == "__main__":
    app.run()
