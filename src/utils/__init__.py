"""
Utilidades del proyecto
"""

from .config import (
    PROJECT_ROOT,
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    RESULTS_DIR,
    FIGURES_DIR,
    REPORTS_DIR,
    DASK_CONFIG,
    EXPERIMENT_CONFIG,
    get_data_path,
    get_result_path
)

__all__ = [
    'PROJECT_ROOT',
    'DATA_DIR',
    'RAW_DATA_DIR',
    'PROCESSED_DATA_DIR',
    'RESULTS_DIR',
    'FIGURES_DIR',
    'REPORTS_DIR',
    'DASK_CONFIG',
    'EXPERIMENT_CONFIG',
    'get_data_path',
    'get_result_path'
]

