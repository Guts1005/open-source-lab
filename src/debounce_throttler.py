"""Event debouncer and throttler for high-frequency input streams."""
import time

class DebounceThrottler:
    def __init__(self, delay_ms: float):
        self.delay_sec = delay_ms / 1000.0
        self.last_run = 0.0

    def should_execute(self) -> bool:
        now = time.monotonic()
        if now - self.last_run >= self.delay_sec:
            self.last_run = now
            return True
        return False
