"""Cache-line alignment padding helper to mitigate multi-core false sharing."""
class CacheLinePadded:
    def __init__(self, value, pad_bytes: int = 64):
        self.value = value
        self._padding = bytearray(pad_bytes)

    def read(self):
        return self.value

    def write(self, new_val):
        self.value = new_val
