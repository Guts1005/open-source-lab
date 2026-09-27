"""High-resolution latency percentile histogram for benchmarks."""
import math

class LatencyHistogram:
    def __init__(self, precision: int = 3):
        self.samples = []
        self.precision = precision

    def record(self, latency_ms: float):
        self.samples.append(latency_ms)

    def percentile(self, p: float) -> float:
        if not self.samples:
            return 0.0
        sorted_samples = sorted(self.samples)
        k = (len(sorted_samples) - 1) * (p / 100.0)
        f = math.floor(k)
        c = math.ceil(k)
        if f == c:
            return sorted_samples[int(k)]
        d0 = sorted_samples[int(f)] * (c - k)
        d1 = sorted_samples[int(c)] * (k - f)
        return round(d0 + d1, self.precision)
