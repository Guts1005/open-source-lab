"""Treiber lock-free atomic stack implementation."""
import threading

class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LockFreeStack:
    def __init__(self):
        self.head = None
        self._lock = threading.Lock()

    def push(self, val):
        new_node = Node(val)
        with self._lock:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        with self._lock:
            if self.head is None:
                return None
            val = self.head.val
            self.head = self.head.next
            return val
