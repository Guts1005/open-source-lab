"""Streaming byte chunker for continuous packet boundaries."""
def chunk_stream(stream_bytes: bytes, chunk_size: int = 4096):
    for i in range(0, len(stream_bytes), chunk_size):
        yield stream_bytes[i:i + chunk_size]
