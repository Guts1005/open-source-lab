# Open Source Systems Engineering Lab 🔬

A high-performance benchmark suite and algorithmic primitives laboratory designed for zero-allocation data structures, high-resolution telemetry, and lock-free concurrency testing.

## 📦 Benchmark Primitives

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

## 🧪 Discussions & Community

Visit the [Discussions Tab](https://github.com/Guts1005/open-source-lab/discussions) to review architectural Q&As and benchmark design patterns.
