"""Binary min-heap task priority queue."""
import heapq

class PriorityTaskQueue:
    def __init__(self):
        self._heap = []
        self._counter = 0

    def push(self, priority: int, task):
        heapq.heappush(self._heap, (priority, self._counter, task))
        self._counter += 1

    def pop(self):
        if not self._heap:
            return None
        return heapq.heappop(self._heap)[2]
