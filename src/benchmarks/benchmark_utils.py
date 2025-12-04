"""
Utilidades para benchmarking y medición de rendimiento
"""

import time
import psutil
import os
from contextlib import contextmanager
from typing import Dict, Any

@contextmanager
def measure_performance(operation_name: str):
    """
    Context manager para medir tiempo y memoria de una operación
    
    Usage:
        with measure_performance("mi_operacion") as perf:
            # tu código aquí
            result = hacer_algo()
        print(f"Tiempo: {perf['time']:.2f}s, Memoria: {perf['memory']:.2f}MB")
    """
    process = psutil.Process(os.getpid())
    mem_before = process.memory_info().rss / (1024 ** 2)  # MB
    start_time = time.time()
    
    performance = {
        'operation': operation_name,
        'time': 0.0,
        'memory_before': mem_before,
        'memory_after': 0.0,
        'memory_used': 0.0,
        'memory_peak': 0.0
    }
    
    try:
        yield performance
    finally:
        end_time = time.time()
        mem_after = process.memory_info().rss / (1024 ** 2)  # MB
        
        performance['time'] = end_time - start_time
        performance['memory_after'] = mem_after
        performance['memory_used'] = mem_after - mem_before
        performance['memory_peak'] = mem_after  # Simplificado

def format_time(seconds: float) -> str:
    """Formatea tiempo en formato legible"""
    if seconds < 1:
        return f"{seconds*1000:.2f} ms"
    elif seconds < 60:
        return f"{seconds:.2f} s"
    else:
        mins = int(seconds // 60)
        secs = seconds % 60
        return f"{mins}m {secs:.2f}s"

def format_memory(mb: float) -> str:
    """Formatea memoria en formato legible"""
    if mb < 1024:
        return f"{mb:.2f} MB"
    else:
        return f"{mb/1024:.2f} GB"

def compare_results(pandas_perf: Dict[str, Any], dask_perf: Dict[str, Any]) -> Dict[str, Any]:
    """Compara resultados de Pandas y Dask"""
    comparison = {
        'speedup': pandas_perf['time'] / dask_perf['time'] if dask_perf['time'] > 0 else 0,
        'memory_ratio': pandas_perf['memory_used'] / dask_perf['memory_used'] if dask_perf['memory_used'] > 0 else 0,
        'time_difference': pandas_perf['time'] - dask_perf['time'],
        'memory_difference': pandas_perf['memory_used'] - dask_perf['memory_used']
    }
    
    return comparison

