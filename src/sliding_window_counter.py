"""Sliding window counter for granular rate limits."""
import time
from collections import deque

class SlidingWindowCounter:
    def __init__(self, window_sec: float, max_requests: int):
        self.window = window_sec
        self.limit = max_requests
        self.timestamps = deque()

    def allow(self) -> bool:
        now = time.monotonic()
        while self.timestamps and now - self.timestamps[0] > self.window:
            self.timestamps.popleft()
        if len(self.timestamps) < self.limit:
            self.timestamps.append(now)
            return True
        return False
