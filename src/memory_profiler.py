"""
High-resolution memory allocation and throughput micro-profiler.
Designed for measuring latency and RSS overhead during continuous buffer allocations.
"""

import time
import os
import psutil

class MemoryProfiler:
    def __init__(self):
        self.process = psutil.Process(os.getpid())
        self.baseline_rss = 0

    def start(self):
        self.baseline_rss = self.process.memory_info().rss
        self.start_time = time.perf_counter_ns()

    def snapshot(self):
        current_rss = self.process.memory_info().rss
        elapsed_ns = time.perf_counter_ns() - self.start_time
        return {
            "rss_delta_mb": (current_rss - self.baseline_rss) / (1024 * 1024),
            "elapsed_ms": elapsed_ns / 1_000_000,
        }

if __name__ == "__main__":
    profiler = MemoryProfiler()
    profiler.start()
    buf = [bytearray(1024 * 64) for _ in range(100)]
    stats = profiler.snapshot()
    print("Memory Allocation Profiler Output:", stats)
