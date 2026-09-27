"""Hazard pointer registry for safe lock-free memory reclamation."""
class HazardPointerManager:
    def __init__(self, max_threads: int = 16):
        self.pointers = [None] * max_threads

    def acquire(self, thread_id: int, node):
        self.pointers[thread_id] = node

    def release(self, thread_id: int):
        self.pointers[thread_id] = None

    def is_protected(self, node) -> bool:
        return node in self.pointers
