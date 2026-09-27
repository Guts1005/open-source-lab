"""Bitwise Bloom filter for constant-time negative lookups."""
import hashlib

class BloomFilter:
    def __init__(self, size: int = 10000, hash_count: int = 5):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, item: str):
        for i in range(self.hash_count):
            h = int(hashlib.md5(f"{item}:{i}".encode()).hexdigest(), 16)
            yield h % self.size

    def add(self, item: str):
        for bit_index in self._hashes(item):
            self.bit_array[bit_index] = 1

    def contains(self, item: str) -> bool:
        return all(self.bit_array[idx] == 1 for idx in self._hashes(item))
