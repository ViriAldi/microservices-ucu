import multiprocessing as mp
import hazelcast
import time


def producer(N, dt):
    client = hazelcast.HazelcastClient()
    queue = client.get_queue("distributed-queue-1").blocking()

    for i in range(N):
        queue.put(i)
        print(f"Produced {i}")
        time.sleep(dt)

    client.shutdown()


def consumer(dt, p_num):
    client = hazelcast.HazelcastClient()
    queue = client.get_queue("distributed-queue-1").blocking()

    while True:
        val = queue.take()
        print(f"Consumed {val} by {p_num}")
        time.sleep(dt)


if __name__ == "__main__":
    N = 50
    dt = 0.01

    client = hazelcast.HazelcastClient()
    queue = client.get_queue("distributed-queue-1").blocking()
    queue.clear()

    procs = [
        mp.Process(target=producer, args=(N, dt,)),
        mp.Process(target=consumer, args=(dt, 0,)),
        mp.Process(target=consumer, args=(dt, 1,)),
    ]

    for proc in procs:
        proc.start()
    for proc in procs:
        proc.join()

    client.shutdown()