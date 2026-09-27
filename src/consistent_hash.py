"""Consistent hash ring implementation with deterministic virtual nodes."""
import bisect
import hashlib

class ConsistentHashRing:
    def __init__(self, replicas: int = 100):
        self.replicas = replicas
        self.ring = dict()
        self.sorted_keys = []

    def _hash(self, key: str) -> int:
        return int(hashlib.sha256(key.encode()).hexdigest(), 16)

    def add_node(self, node: str):
        for i in range(self.replicas):
            k = self._hash(f"{node}:{i}")
            self.ring[k] = node
            bisect.insort(self.sorted_keys, k)

    def get_node(self, key: str) -> str:
        if not self.ring:
            return None
        k = self._hash(key)
        idx = bisect.bisect_right(self.sorted_keys, k) % len(self.sorted_keys)
        return self.ring[self.sorted_keys[idx]]
