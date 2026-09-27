"""Concurrent micro-task thread worker pool."""
import queue
import threading

class WorkerPool:
    def __init__(self, num_workers: int = 4):
        self.queue = queue.Queue()
        self.workers = []
        for _ in range(num_workers):
            t = threading.Thread(target=self._worker, daemon=True)
            t.start()
            self.workers.append(t)

    def _worker(self):
        while True:
            func, args, kwargs = self.queue.get()
            try:
                func(*args, **kwargs)
            finally:
                self.queue.task_done()

    def submit(self, func, *args, **kwargs):
        self.queue.put((func, args, kwargs))

    def join(self):
        self.queue.join()
