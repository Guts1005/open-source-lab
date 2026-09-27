"""Binary frame packing utility for protocol serialization."""
import struct

class BytePacker:
    HEADER_FORMAT = "!IIH"

    @staticmethod
    def pack_header(seq_num: int, payload_len: int, flags: int) -> bytes:
        return struct.pack(BytePacker.HEADER_FORMAT, seq_num, payload_len, flags)

    @staticmethod
    def unpack_header(data: bytes) -> tuple:
        return struct.unpack(BytePacker.HEADER_FORMAT, data)
