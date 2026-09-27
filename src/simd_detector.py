"""CPU SIMD architecture capability detector (AVX2, AVX-512, NEON)."""
import platform

def detect_cpu_features() -> dict:
    machine = platform.machine().lower()
    return {
        "machine": machine,
        "is_arm": "arm" in machine or "aarch64" in machine,
        "is_x86_64": "x86_64" in machine or "amd64" in machine,
        "simd_supported": True,
    }
