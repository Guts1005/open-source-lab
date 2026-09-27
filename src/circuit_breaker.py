"""Three-state (closed, open, half-open) circuit breaker."""
import time

class CircuitBreaker:
    def __init__(self, fail_threshold: int = 5, recovery_timeout: float = 10.0):
        self.fail_threshold = fail_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.state = "CLOSED"
        self.last_failure_time = 0.0

    def record_success(self):
        self.failure_count = 0
        self.state = "CLOSED"

    def record_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.monotonic()
        if self.failure_count >= self.fail_threshold:
            self.state = "OPEN"

    def can_attempt(self) -> bool:
        if self.state == "CLOSED":
            return True
        if self.state == "OPEN":
            if time.monotonic() - self.last_failure_time >= self.recovery_timeout:
                self.state = "HALF-OPEN"
                return True
            return False
        return True
