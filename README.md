# Open Source Systems Engineering Lab 🔬

A high-performance benchmark suite and algorithmic primitives laboratory designed for zero-allocation data structures, high-resolution telemetry, lock-free concurrency, and distributed systems algorithms.

## 📦 Benchmark Primitives (24 Components)

| Component | Path | Description |
| :--- | :--- | :--- |
| **Memory Profiler** | `src/memory_profiler.py` | Tracemalloc-based differential heap snapshot harness |
| **Latency Histogram** | `src/latency_histogram.py` | High-resolution percentile tracking (`p50`, `p90`, `p99`) |
| **Ring Buffer** | `src/ring_buffer.py` | Zero-allocation bounded circular buffer |
| **Token Bucket** | `src/token_bucket.py` | Monotonic rate-limiting algorithm |
| **Worker Pool** | `src/thread_pool.py` | Concurrent micro-task execution queue |
| **LRU Cache** | `src/lru_cache.py` | Doubly-linked key-value cache |
| **SIMD Detector** | `src/simd_detector.py` | Architecture vector instruction probe |
| **Cache Line Pad** | `src/cache_line_pad.py` | 64-byte boundary padding to mitigate multi-core false sharing |
| **Exponential Backoff** | `src/exponential_backoff.py` | Full-jitter randomized exponential retry backoff |
| **CRC32 Validator** | `src/checksum_crc32.py` | Streaming cyclic redundancy integrity checker |
| **Streaming Chunker** | `src/streaming_chunker.py` | Zero-copy packet boundary streaming chunker |
| **Arena Allocator** | `src/arena_allocator.py` | Linear bump arena allocator with bulk reset |
| **Bloom Filter** | `src/bloom_filter.py` | Bitwise Bloom filter with multi-hash probing |
| **Memory Fence** | `src/memory_fence.py` | Atomic memory barrier execution harness |
| **Hazard Pointer** | `src/hazard_pointer.py` | Lock-free reader hazard pointer tracker |
| **Debounce Throttler** | `src/debounce_throttler.py` | Microsecond event trailing throttler |
| **Consistent Hash Ring** | `src/consistent_hash.py` | Hash ring with deterministic virtual nodes |
| **Priority Heap** | `src/priority_heap.py` | Binary min-heap priority task queue |
| **Prefix Trie** | `src/trie_lookup.py` | High-speed prefix trie for route matching |
| **Sliding Window Counter** | `src/sliding_window_counter.py` | Memory-bounded rate limiter counter |
| **Byte Packer** | `src/byte_packer.py` | Binary frame struct serializer |
| **Circuit Breaker** | `src/circuit_breaker.py` | Tri-state fault tolerance circuit breaker |
| **MurmurHash3** | `src/murmur3_hasher.py` | 32-bit fast integer non-cryptographic hasher |
| **Lock-Free Stack** | `src/lock_free_stack.py` | Treiber lock-free atomic stack |

## 🧪 Discussions & Architecture Q&A (16 Topics)

Visit the [Discussions Tab](https://github.com/Guts1005/open-source-lab/discussions) to review 16 curated architectural Q&As covering memory barriers, Nagle's algorithm, mmap, Bloom filters, hazard pointers, branch prediction, and arena allocators.
