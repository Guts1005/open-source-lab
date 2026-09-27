"""Linear arena allocator for zero-fragmentation high-throughput cycles."""
class ArenaAllocator:
    def __init__(self, size_bytes: int = 1048576):
        self.buffer = bytearray(size_bytes)
        self.capacity = size_bytes
        self.offset = 0

    def allocate(self, size: int) -> memoryview:
        if self.offset + size > self.capacity:
            raise MemoryError("Arena allocator exhausted")
        allocated = memoryview(self.buffer)[self.offset:self.offset + size]
        self.offset += size
        return allocated

    def reset(self):
        self.offset = 0
