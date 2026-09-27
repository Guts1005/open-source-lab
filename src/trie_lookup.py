"""Prefix trie for high-speed routing and URL pattern matching."""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_terminal = False
        self.payload = None

class PrefixTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, path: str, payload):
        node = self.root
        for part in path.strip("/").split("/"):
            if part not in node.children:
                node.children[part] = TrieNode()
            node = node.children[part]
        node.is_terminal = True
        node.payload = payload

    def match(self, path: str):
        node = self.root
        for part in path.strip("/").split("/"):
            if part not in node.children:
                return None
            node = node.children[part]
        return node.payload if node.is_terminal else None
