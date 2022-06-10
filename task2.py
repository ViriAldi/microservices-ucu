import multiprocessing as mp
import hazelcast
import time


def update_no_lock(n, dt):
    client = hazelcast.HazelcastClient()
    dist_map = client.get_map("distributed-map-1").blocking()

    key = "key"
    for k in range(n):
        val = dist_map.get(key)
        time.sleep(dt)
        val += 1
        dist_map.put(key, val)

    client.shutdown()


def update_pessimistic_lock(n, dt):
    client = hazelcast.HazelcastClient()
    dist_map = client.get_map("distributed-map-1").blocking()

    key = "key"
    for k in range(n):
        dist_map.lock(key)

        val = dist_map.get(key)
        time.sleep(dt)
        val += 1
        dist_map.put(key, val)

        dist_map.unlock(key)

    client.shutdown()


def update_optimistic_lock(n, dt):
    client = hazelcast.HazelcastClient()
    dist_map = client.get_map("distributed-map-1").blocking()

    key = "key"
    for k in range(n):
        while True:

            val = dist_map.get(key)
            val_old = val
            time.sleep(dt)
            val += 1
            if dist_map.replace_if_same(key, val_old, val):
                break

    client.shutdown()


if __name__ == "__main__":
    client = hazelcast.HazelcastClient()
    dist_map = client.get_map("distributed-map-1").blocking()

    N = 1000
    nproc = 3
    dt = 0.01
    key = "key"

    for func, name in zip(
            [update_no_lock, update_pessimistic_lock, update_optimistic_lock],
            ["No lock", "Pessimistic lock:", "Optimistic lock:"]
    ):
        t_start = time.time()

        dist_map.put(key, 0)
        procs = []
        for i in range(nproc):
            proc = mp.Process(target=func, args=(N, dt,))
            proc.start()
            procs.append(proc)
        for proc in procs:
            proc.join()

        t_end = time.time()

        print(f"{name} result: {dist_map.get(key)}")
        print(f"{name} time: {(t_end - t_start):.3f}s")

    client.shutdown()
