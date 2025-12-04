"""
Módulo de benchmarking y utilidades de medición
"""

from .benchmark_utils import (
    measure_performance,
    format_time,
    format_memory,
    compare_results
)

__all__ = [
    'measure_performance',
    'format_time',
    'format_memory',
    'compare_results'
]

