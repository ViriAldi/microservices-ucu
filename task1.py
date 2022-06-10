import hazelcast
import random


if __name__ == "__main__":
    client = hazelcast.HazelcastClient()
    dist_map = client.get_map("distributed-map").blocking()

    N = 1000
    min_val = 0
    max_val = 10**6

    for key in range(N):
        dist_map.put(key, random.randint(min_val, max_val))

    client.shutdown()
