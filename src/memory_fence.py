"""Memory barrier simulation harness for verifying instruction order."""
import threading

class MemoryFence:
    def __init__(self):
        self.flag = False
        self.data = 0
        self._lock = threading.Lock()

    def store_release(self, val: int):
        with self._lock:
            self.data = val
            self.flag = True

    def load_acquire(self) -> tuple:
        with self._lock:
            return (self.flag, self.data)
