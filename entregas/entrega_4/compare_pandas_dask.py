"""
Script para comparar rendimiento entre Pandas y Dask
Entrega 4: Implementación de las mismas tareas con Pandas para comparación
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
import numpy as np
import time
import psutil
import os
from pathlib import Path
import sys

# Agregar el directorio raíz al path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.config import RAW_DATA_DIR, PROCESSED_DATA_DIR, get_data_path

class PerformanceBenchmark:
    """Clase para realizar benchmarks de rendimiento"""
    
    def __init__(self):
        self.results = {
            'operation': [],
            'method': [],
            'time': [],
            'memory_peak': [],
            'memory_avg': []
        }
    
    def get_memory_usage(self):
        """Obtiene el uso actual de memoria en MB"""
        process = psutil.Process(os.getpid())
        return process.memory_info().rss / (1024 ** 2)  # MB
    
    def benchmark_operation(self, operation_name, pandas_func, dask_func, *args, **kwargs):
        """
        Compara el rendimiento de una operación entre Pandas y Dask
        
        Parameters:
        -----------
        operation_name : str
            Nombre de la operación
        pandas_func : callable
            Función que ejecuta la operación con Pandas
        dask_func : callable
            Función que ejecuta la operación con Dask
        """
        print(f"\n{'='*70}")
        print(f"BENCHMARK: {operation_name.upper()}")
        print(f"{'='*70}")
        
        # Benchmark Pandas
        print(f"\n[PANDAS] Ejecutando {operation_name}...")
        mem_before = self.get_memory_usage()
        start_time = time.time()
        
        try:
            pandas_result = pandas_func(*args, **kwargs)
            pandas_time = time.time() - start_time
            mem_after = self.get_memory_usage()
            pandas_memory = max(0.0, mem_after - mem_before)  # Asegurar que no sea negativo
            
            print(f"  ✓ Completado en {pandas_time:.2f} segundos")
            print(f"  Memoria usada: {pandas_memory:.2f} MB")
            
            self.results['operation'].append(operation_name)
            self.results['method'].append('Pandas')
            self.results['time'].append(pandas_time)
            self.results['memory_peak'].append(mem_after)
            self.results['memory_avg'].append(pandas_memory)
            
        except MemoryError:
            print(f"  ✗ ERROR: Memoria insuficiente")
            pandas_time = None
            pandas_result = None
        
        # Benchmark Dask
        print(f"\n[DASK] Ejecutando {operation_name}...")
        mem_before = self.get_memory_usage()
        start_time = time.time()
        
        try:
            dask_result = dask_func(*args, **kwargs)
            dask_time = time.time() - start_time
            mem_after = self.get_memory_usage()
            dask_memory = max(0.0, mem_after - mem_before)  # Asegurar que no sea negativo
            
            print(f"  ✓ Completado en {dask_time:.2f} segundos")
            print(f"  Memoria usada: {dask_memory:.2f} MB")
            
            self.results['operation'].append(operation_name)
            self.results['method'].append('Dask')
            self.results['time'].append(dask_time)
            self.results['memory_peak'].append(mem_after)
            self.results['memory_avg'].append(dask_memory)
            
        except Exception as e:
            print(f"  ✗ ERROR: {e}")
            dask_time = None
            dask_result = None
        
        # Comparación
        if pandas_time and dask_time:
            speedup = pandas_time / dask_time if dask_time > 0 else float('inf')
            # Calcular ratio de memoria de forma segura
            if pandas_memory > 0 and dask_memory > 0:
                memory_ratio = pandas_memory / dask_memory
            elif pandas_memory > 0 and dask_memory == 0:
                memory_ratio = float('inf')  # Pandas usa memoria, Dask no
            elif pandas_memory == 0 and dask_memory > 0:
                memory_ratio = 0  # Pandas no usa memoria, Dask sí
            else:
                memory_ratio = 1.0  # Ambos usan 0 (o muy poco)
            
            print(f"\n{'='*70}")
            print("COMPARACIÓN")
            print(f"{'='*70}")
            print(f"Velocidad:")
            if speedup == float('inf'):
                print(f"  Dask es instantáneo (Pandas: {pandas_time:.2f}s)")
            elif speedup > 1:
                print(f"  Dask es {speedup:.2f}x más rápido")
            elif speedup > 0:
                print(f"  Pandas es {1/speedup:.2f}x más rápido")
            else:
                print(f"  Pandas: {pandas_time:.2f}s, Dask: {dask_time:.2f}s")
            
            print(f"\nMemoria:")
            if memory_ratio == float('inf'):
                print(f"  Dask no usa memoria medible (Pandas: {pandas_memory:.2f} MB)")
            elif memory_ratio > 1:
                print(f"  Dask usa {memory_ratio:.2f}x menos memoria")
            elif memory_ratio > 0:
                inverse_ratio = 1 / memory_ratio
                print(f"  Pandas usa {inverse_ratio:.2f}x menos memoria")
            else:
                print(f"  Pandas no usa memoria medible (Dask: {dask_memory:.2f} MB)")
            if memory_ratio == 1.0 and pandas_memory == 0 and dask_memory == 0:
                print("  (Ambos usan memoria despreciable)")
        
        return pandas_result, dask_result
    
    def get_results_df(self):
        """Retorna los resultados como DataFrame"""
        return pd.DataFrame(self.results)

def benchmark_reading(filepath, sample_size=None):
    """Compara la lectura de datos"""
    benchmark = PerformanceBenchmark()
    
    def pandas_read():
        if sample_size:
            return pd.read_csv(filepath, nrows=sample_size)
        return pd.read_csv(filepath)
    
    def dask_read():
        ddf = dd.read_csv(filepath, blocksize='100MB')
        if sample_size:
            return ddf.head(sample_size)
        return ddf
    
    pandas_result, dask_result = benchmark.benchmark_operation(
        "Lectura de Datos",
        pandas_read,
        dask_read
    )
    
    return benchmark, pandas_result, dask_result

def benchmark_filtering(df_pandas, ddf_dask, filter_condition):
    """Compara el filtrado de datos"""
    benchmark = PerformanceBenchmark()
    
    def pandas_filter():
        return df_pandas[filter_condition(df_pandas)]
    
    def dask_filter():
        return ddf_dask[filter_condition(ddf_dask)].compute()
    
    pandas_result, dask_result = benchmark.benchmark_operation(
        "Filtrado de Datos",
        pandas_filter,
        dask_filter
    )
    
    return benchmark, pandas_result, dask_result

def benchmark_groupby(df_pandas, ddf_dask, groupby_col, agg_col):
    """Compara operaciones groupby"""
    benchmark = PerformanceBenchmark()
    
    def pandas_groupby():
        return df_pandas.groupby(groupby_col)[agg_col].mean()
    
    def dask_groupby():
        return ddf_dask.groupby(groupby_col)[agg_col].mean().compute()
    
    pandas_result, dask_result = benchmark.benchmark_operation(
        "Agrupación (GroupBy)",
        pandas_groupby,
        dask_groupby
    )
    
    return benchmark, pandas_result, dask_result

def benchmark_aggregation(df_pandas, ddf_dask):
    """Compara agregaciones"""
    benchmark = PerformanceBenchmark()
    
    numeric_cols = df_pandas.select_dtypes(include=[np.number]).columns.tolist()
    if len(numeric_cols) == 0:
        print("⚠ No hay columnas numéricas para agregar")
        return benchmark, None, None
    
    agg_col = numeric_cols[0]
    
    def pandas_agg():
        return df_pandas[agg_col].sum()
    
    def dask_agg():
        return ddf_dask[agg_col].sum().compute()
    
    pandas_result, dask_result = benchmark.benchmark_operation(
        "Agregación (Suma)",
        pandas_agg,
        dask_agg
    )
    
    return benchmark, pandas_result, dask_result

def main():
    """Función principal"""
    print("\n" + "="*70)
    print("ENTREGA 4: COMPARACIÓN PANDAS vs DASK")
    print("="*70 + "\n")
    
    # Buscar archivo de datos
    csv_files = list(RAW_DATA_DIR.glob("*.csv"))
    
    if len(csv_files) == 0:
        print("⚠ No se encontraron archivos CSV en data/raw/")
        print("  Coloca un dataset para realizar la comparación")
        return
    
    filepath = csv_files[0]
    file_size_gb = filepath.stat().st_size / (1024**3)
    
    print(f"Archivo: {filepath.name}")
    print(f"Tamaño: {file_size_gb:.2f} GB")
    
    # Determinar tamaño de muestra si el archivo es muy grande
    sample_size = None
    if file_size_gb > 2.0:
        print("\n⚠ Archivo muy grande. Usando muestra de 500,000 filas para Pandas")
        sample_size = 500000
    
    # Benchmark 1: Lectura
    benchmark1, df_pandas, ddf_dask = benchmark_reading(filepath, sample_size)
    
    if df_pandas is None or ddf_dask is None:
        print("\n✗ No se pudo completar la lectura. Abortando comparación.")
        return
    
    # Si usamos muestra, limitar Dask también
    if sample_size:
        try:
            ddf_sample = ddf_dask.head(sample_size)
            ddf_dask = dd.from_pandas(ddf_sample, npartitions=4)
        except:
            # Si head() no funciona, usar take
            ddf_dask = ddf_dask.take(range(min(sample_size, len(ddf_dask))))
            ddf_dask = dd.from_pandas(ddf_dask, npartitions=4)
    
    # Benchmark 2: Filtrado (si hay columnas numéricas)
    numeric_cols = df_pandas.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        filter_col = numeric_cols[0]
        filter_condition = lambda df: df[filter_col] > df[filter_col].quantile(0.5)
        
        benchmark2, _, _ = benchmark_filtering(df_pandas, ddf_dask, filter_condition)
        
        # Combinar resultados
        for key in benchmark1.results:
            benchmark1.results[key].extend(benchmark2.results[key])
    
    # Benchmark 3: GroupBy (si hay columnas categóricas)
    categorical_cols = df_pandas.select_dtypes(include=['object', 'category']).columns
    numeric_cols = df_pandas.select_dtypes(include=[np.number]).columns
    
    if len(categorical_cols) > 0 and len(numeric_cols) > 0:
        groupby_col = categorical_cols[0]
        agg_col = numeric_cols[0]
        
        benchmark3, _, _ = benchmark_groupby(df_pandas, ddf_dask, groupby_col, agg_col)
        
        # Combinar resultados
        for key in benchmark1.results:
            benchmark1.results[key].extend(benchmark3.results[key])
    
    # Benchmark 4: Agregación
    benchmark4, _, _ = benchmark_aggregation(df_pandas, ddf_dask)
    
    # Combinar resultados
    for key in benchmark1.results:
        benchmark1.results[key].extend(benchmark4.results[key])
    
    # Resumen final
    results_df = benchmark1.get_results_df()
    
    print(f"\n{'='*70}")
    print("RESUMEN DE RESULTADOS")
    print(f"{'='*70}")
    print("\n" + results_df.to_string(index=False))
    
    # Guardar resultados
    output_path = PROCESSED_DATA_DIR / "benchmark_results.csv"
    results_df.to_csv(output_path, index=False)
    print(f"\n✓ Resultados guardados en: {output_path}")
    
    print("\n" + "="*70)
    print("COMPARACIÓN COMPLETADA")
    print("="*70)
    print("\nPróximos pasos:")
    print("  - Ejecutar: python entregas/entrega_5/visualize_results.py")
    print("  - Para generar visualizaciones y análisis final\n")

if __name__ == "__main__":
    main()

