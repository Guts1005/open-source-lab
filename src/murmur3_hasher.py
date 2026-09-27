"""MurmurHash3 32-bit non-cryptographic fast hash."""
def murmur3_32(key: bytes, seed: int = 0) -> int:
    c1 = 0xcc9e2d51
    c2 = 0x1b873593
    h1 = seed
    length = len(key)
    nblocks = length // 4
    for i in range(nblocks):
        k1 = int.from_bytes(key[i*4:(i+1)*4], "little")
        k1 = (k1 * c1) & 0xFFFFFFFF
        k1 = ((k1 << 15) | (k1 >> 17)) & 0xFFFFFFFF
        k1 = (k1 * c2) & 0xFFFFFFFF
        h1 ^= k1
        h1 = ((h1 << 13) | (h1 >> 19)) & 0xFFFFFFFF
        h1 = ((h1 * 5) + 0xe6546b64) & 0xFFFFFFFF
    h1 ^= length
    h1 ^= (h1 >> 16)
    h1 = (h1 * 0x85ebca6b) & 0xFFFFFFFF
    h1 ^= (h1 >> 13)
    h1 = (h1 * 0xc2b2ae35) & 0xFFFFFFFF
    h1 ^= (h1 >> 16)
    return h1
