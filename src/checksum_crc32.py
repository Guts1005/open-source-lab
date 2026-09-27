"""Streaming CRC32 cyclic redundancy check for data blocks."""
import zlib

class CRC32Validator:
    def __init__(self):
        self.checksum = 0

    def update(self, data: bytes):
        self.checksum = zlib.crc32(data, self.checksum)
        return self.checksum

    def digest(self) -> int:
        return self.checksum
