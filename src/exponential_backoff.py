"""Full-jitter exponential retry backoff algorithm."""
import random

def calculate_backoff(attempt: int, base: float = 0.5, cap: float = 30.0) -> float:
    exp = min(cap, base * (2 ** attempt))
    return random.uniform(0, exp)
