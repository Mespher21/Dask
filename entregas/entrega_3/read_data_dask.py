"""
Script para leer datasets grandes usando Dask
Entrega 3: Lectura y primeras transformaciones con Dask
"""

try:
    import dask.dataframe as dd
except ImportError:
    print("="*70)
    print("ERROR: Dask no está instalado")
    print("="*70)
    print("\nPor favor, instala Dask ejecutando:")
    print("  pip install dask")
    print("\nO instala todas las dependencias:")
    print("  pip install -r requirements.txt")
    print("\nTambién puedes ejecutar:")
    print("  python check_dependencies.py")
    sys.exit(1)

import pandas as pd
import time
import os
from pathlib import Path
import sys

# Agregar el directorio raíz al path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.config import RAW_DATA_DIR, get_data_path

def read_csv_with_dask(filepath, chunksize='100MB', **kwargs):
    """
    Lee un archivo CSV usando Dask DataFrame
    
    Parameters:
    -----------
    filepath : str o Path
        Ruta al archivo CSV
    chunksize : str o int
        Tamaño de cada partición (ej: '100MB', 1000000)
    **kwargs : dict
        Argumentos adicionales para dd.read_csv
    """
    print(f"\n{'='*70}")
    print("LECTURA CON DASK")
    print(f"{'='*70}")
    
    print(f"\nArchivo: {filepath}")
    print(f"Tamaño del archivo: {os.path.getsize(filepath) / (1024**3):.2f} GB")
    print(f"Chunk size: {chunksize}")
    
    start_time = time.time()
    
    # Leer con Dask
    ddf = dd.read_csv(
        filepath,
        blocksize=chunksize,
        **kwargs
    )
    
    read_time = time.time() - start_time
    
    print(f"\n✓ Lectura completada en {read_time:.2f} segundos")
    print(f"Número de particiones: {ddf.npartitions}")
    print(f"División: {ddf.divisions[:3]}... (mostrando primeras 3)")
    
    # Información del DataFrame (sin computar todo)
    print(f"\nInformación del DataFrame (sin cargar en memoria):")
    print(f"  Columnas: {list(ddf.columns)}")
    print(f"  Tipos de datos: {dict(ddf.dtypes)}")
    
    # Obtener número de filas (esto sí computa)
    print("\nContando filas (esto puede tardar)...")
    start_count = time.time()
    n_rows = len(ddf)
    count_time = time.time() - start_count
    print(f"  Total de filas: {n_rows:,}")
    print(f"  Tiempo de conteo: {count_time:.2f} segundos")
    
    # Mostrar primeras filas
    print("\nPrimeras 5 filas:")
    print(ddf.head())
    
    return ddf, read_time

def read_csv_with_pandas(filepath, **kwargs):
    """
    Lee un archivo CSV usando Pandas (para comparación)
    
    Parameters:
    -----------
    filepath : str o Path
        Ruta al archivo CSV
    **kwargs : dict
        Argumentos adicionales para pd.read_csv
    """
    print(f"\n{'='*70}")
    print("LECTURA CON PANDAS (COMPARACIÓN)")
    print(f"{'='*70}")
    
    print(f"\nArchivo: {filepath}")
    file_size = os.path.getsize(filepath) / (1024**3)
    print(f"Tamaño del archivo: {file_size:.2f} GB")
    
    if file_size > 2.0:
        print("\n⚠ ADVERTENCIA: El archivo es muy grande para Pandas.")
        print("  Pandas carga todo en memoria, esto puede fallar o ser muy lento.")
        print("  Se intentará leer solo las primeras filas para comparación...")
        
        start_time = time.time()
        df = pd.read_csv(filepath, nrows=100000, **kwargs)
        read_time = time.time() - start_time
        
        print(f"\n✓ Lectura de muestra (100,000 filas) completada en {read_time:.2f} segundos")
        print(f"  Filas leídas: {len(df):,}")
        print(f"  Columnas: {list(df.columns)}")
        
        return df, read_time, "sample"
    
    start_time = time.time()
    
    try:
        df = pd.read_csv(filepath, **kwargs)
        read_time = time.time() - start_time
        
        print(f"\n✓ Lectura completada en {read_time:.2f} segundos")
        print(f"  Total de filas: {len(df):,}")
        print(f"  Columnas: {list(df.columns)}")
        print(f"  Memoria usada: {df.memory_usage(deep=True).sum() / (1024**2):.2f} MB")
        
        return df, read_time, "full"
    
    except MemoryError:
        print("\n✗ ERROR: Memoria insuficiente para cargar el archivo completo con Pandas")
        print("  Esto demuestra la limitación de Pandas con archivos grandes")
        return None, None, "error"

def compare_reading_methods(filepath, chunksize='100MB'):
    """
    Compara el tiempo de lectura entre Dask y Pandas
    """
    print(f"\n{'='*70}")
    print("COMPARACIÓN: DASK vs PANDAS - LECTURA DE DATOS")
    print(f"{'='*70}")
    
    # Leer con Dask
    ddf, dask_time = read_csv_with_dask(filepath, chunksize=chunksize)
    
    # Leer con Pandas
    df, pandas_time, pandas_status = read_csv_with_pandas(filepath)
    
    # Comparación
    print(f"\n{'='*70}")
    print("RESUMEN DE COMPARACIÓN")
    print(f"{'='*70}")
    
    print(f"\nDask:")
    print(f"  Tiempo de lectura: {dask_time:.2f} segundos")
    print(f"  Particiones creadas: {ddf.npartitions}")
    print(f"  Memoria: Solo carga chunks cuando se necesitan")
    
    if pandas_status == "full":
        print(f"\nPandas:")
        print(f"  Tiempo de lectura: {pandas_time:.2f} segundos")
        print(f"  Memoria usada: {df.memory_usage(deep=True).sum() / (1024**2):.2f} MB")
        
        speedup = pandas_time / dask_time if dask_time > 0 else 0
        print(f"\nVelocidad:")
        if speedup > 1:
            print(f"  Dask es {speedup:.2f}x más rápido")
        else:
            print(f"  Pandas es {1/speedup:.2f}x más rápido")
    
    elif pandas_status == "sample":
        print(f"\nPandas:")
        print(f"  Tiempo de lectura (muestra): {pandas_time:.2f} segundos")
        print(f"  ⚠ Solo se leyó una muestra debido al tamaño del archivo")
        print(f"  ⚠ Pandas no puede cargar el archivo completo en memoria")
    
    else:
        print(f"\nPandas:")
        print(f"  ✗ No se pudo leer el archivo (memoria insuficiente)")
    
    print(f"\n{'='*70}\n")
    
    return ddf, df

def find_csv_files(directory):
    """Encuentra archivos CSV en el directorio"""
    directory = Path(directory)
    csv_files = list(directory.glob("*.csv"))
    
    if not csv_files:
        print(f"\n⚠ No se encontraron archivos CSV en {directory}")
        print("  Coloca tu dataset en formato CSV en: data/raw/")
        return None
    
    print(f"\nArchivos CSV encontrados en {directory}:")
    for i, file in enumerate(csv_files, 1):
        size_gb = file.stat().st_size / (1024**3)
        print(f"  {i}. {file.name} ({size_gb:.2f} GB)")
    
    return csv_files[0] if len(csv_files) == 1 else csv_files

def main():
    """Función principal"""
    print("\n" + "="*70)
    print("ENTREGA 3: LECTURA DE DATASETS GRANDES CON DASK")
    print("="*70 + "\n")
    
    # Buscar archivos CSV
    csv_file = find_csv_files(RAW_DATA_DIR)
    
    if csv_file is None:
        print("\nPara usar este script:")
        print("1. Descarga un dataset CSV de al menos 1 GB")
        print("2. Colócalo en: data/raw/")
        print("3. Vuelve a ejecutar este script")
        print("\nEjemplo de datasets:")
        print("  - NYC Taxi Trip Data (Kaggle)")
        print("  - Amazon Product Reviews")
        print("  - Google Play Store Apps")
        return
    
    # Si hay múltiples archivos, usar el primero o el más grande
    if isinstance(csv_file, list):
        csv_file = max(csv_file, key=lambda f: f.stat().st_size)
        print(f"\nUsando el archivo más grande: {csv_file.name}")
    
    # Comparar métodos de lectura
    ddf, df = compare_reading_methods(csv_file, chunksize='100MB')
    
    print("\n✓ Proceso completado")
    print("\nPróximos pasos:")
    print("  - Ejecutar: python entregas/entrega_3/transform_data_dask.py")
    print("  - Para realizar transformaciones y limpieza de datos\n")

if __name__ == "__main__":
    main()

