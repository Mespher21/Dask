"""
Configuración centralizada del proyecto
"""

from pathlib import Path

# Directorio raíz del proyecto
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Directorios de datos
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Directorios de resultados
RESULTS_DIR = PROJECT_ROOT / "results"
FIGURES_DIR = RESULTS_DIR / "figures"
REPORTS_DIR = RESULTS_DIR / "reports"

# Configuración de Dask
DASK_CONFIG = {
    'scheduler': 'threads',  # 'threads', 'processes', o 'distributed'
    'num_workers': 4,
    'threads_per_worker': 1,
    'memory_limit': 'auto'
}

# Configuración de experimentos
EXPERIMENT_CONFIG = {
    'min_dataset_size_gb': 1.0,
    'max_dataset_size_gb': 5.0,
    'chunk_size_mb': 100,  # Tamaño de chunks en MB
}

def get_data_path(filename: str) -> Path:
    """Obtiene la ruta completa de un archivo en data/raw"""
    return RAW_DATA_DIR / filename

def get_result_path(filename: str, subdir: str = None) -> Path:
    """Obtiene la ruta completa de un archivo de resultados"""
    if subdir:
        return RESULTS_DIR / subdir / filename
    return RESULTS_DIR / filename

