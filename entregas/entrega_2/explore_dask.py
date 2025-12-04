"""
Script para explorar el funcionamiento básico de Dask
Entrega 2: Revisión del funcionamiento teórico de Dask
"""

import sys

try:
    import dask
    import dask.array as da
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
from pathlib import Path

def demonstrate_dask_arrays():
    """Demuestra el uso básico de Dask Arrays"""
    print("=" * 70)
    print("1. DASK ARRAYS - Procesamiento Paralelo de Arrays")
    print("=" * 70)
    
    # Crear un array grande usando Dask
    print("\nCreando un array Dask de 10,000 x 10,000 elementos...")
    x = da.random.random((10000, 10000), chunks=(1000, 1000))
    print(f"Tipo: {type(x)}")
    print(f"Shape: {x.shape}")
    print(f"Chunks: {x.chunks}")
    print(f"Tamaño en memoria (estimado): {x.nbytes / 1e9:.2f} GB")
    
    # Operación diferida
    print("\nRealizando operación (suma de cuadrados)...")
    result = (x ** 2).sum()
    print(f"Resultado (computación diferida): {result}")
    print(f"Tipo del resultado: {type(result)}")
    
    # Computar el resultado
    print("\nComputando el resultado...")
    start = time.time()
    computed_result = result.compute()
    elapsed = time.time() - start
    print(f"Resultado computado: {computed_result:.2f}")
    print(f"Tiempo de ejecución: {elapsed:.2f} segundos")
    print()

def demonstrate_dask_dataframes():
    """Demuestra el uso básico de Dask DataFrames"""
    print("=" * 70)
    print("2. DASK DATAFRAMES - Procesamiento Paralelo de DataFrames")
    print("=" * 70)
    
    # Crear un DataFrame de ejemplo
    print("\nCreando un DataFrame de ejemplo con 1,000,000 de filas...")
    n_rows = 1_000_000
    df = pd.DataFrame({
        'id': range(n_rows),
        'value1': np.random.randn(n_rows),
        'value2': np.random.randn(n_rows),
        'category': np.random.choice(['A', 'B', 'C', 'D'], n_rows)
    })
    
    # Convertir a Dask DataFrame
    ddf = dd.from_pandas(df, npartitions=4)
    print(f"DataFrame Pandas: {df.shape}")
    print(f"Dask DataFrame: {ddf.shape}")
    print(f"Número de particiones: {ddf.npartitions}")
    print(f"División: {ddf.divisions}")
    
    # Operaciones diferidas
    print("\nRealizando operaciones...")
    result = ddf.groupby('category')['value1'].mean()
    print(f"Resultado (computación diferida): {result}")
    print(f"Tipo: {type(result)}")
    
    # Computar
    print("\nComputando el resultado...")
    start = time.time()
    computed_result = result.compute()
    elapsed = time.time() - start
    print(f"Resultado computado:\n{computed_result}")
    print(f"Tiempo de ejecución: {elapsed:.2f} segundos")
    print()

def demonstrate_lazy_evaluation():
    """Demuestra la evaluación diferida (lazy evaluation) de Dask"""
    print("=" * 70)
    print("3. EVALUACIÓN DIFERIDA (LAZY EVALUATION)")
    print("=" * 70)
    
    # Crear operaciones complejas
    print("\nCreando un grafo de tareas complejo...")
    x = da.random.random((5000, 5000), chunks=(500, 500))
    y = da.random.random((5000, 5000), chunks=(500, 500))
    
    # Múltiples operaciones
    z1 = x + y
    z2 = x * y
    z3 = z1 ** 2
    result = z3.sum() + z2.sum()
    
    print(f"Operación creada: (x+y)².sum() + (x*y).sum()")
    print(f"Tipo: {type(result)}")
    print(f"¿Ya está computado? No, es una operación diferida")
    
    # Visualizar el grafo de tareas
    print("\nVisualizando el grafo de tareas...")
    print("(El grafo muestra cómo Dask organiza las operaciones)")
    try:
        result.visualize(filename='results/figures/dask_graph.png', optimize_graph=True)
        print("✓ Grafo guardado en: results/figures/dask_graph.png")
    except Exception as e:
        print(f"⚠ No se pudo generar el grafo: {e}")
    
    # Computar
    print("\nComputando el resultado...")
    start = time.time()
    computed = result.compute()
    elapsed = time.time() - start
    print(f"Resultado: {computed:.2f}")
    print(f"Tiempo: {elapsed:.2f} segundos")
    print()

def demonstrate_scheduler_info():
    """Muestra información sobre el scheduler de Dask"""
    print("=" * 70)
    print("4. SCHEDULER DE DASK")
    print("=" * 70)
    
    # Información del scheduler por defecto
    print("\nScheduler por defecto: Threaded")
    print("Dask puede usar diferentes schedulers:")
    print("  - threaded: Para operaciones con GIL liberado")
    print("  - processes: Para paralelismo verdadero")
    print("  - distributed: Para clústeres")
    
    # Configurar scheduler
    print("\nConfigurando scheduler para múltiples workers...")
    with dask.config.set({'scheduler': 'threads', 'num_workers': 4}):
        print("Scheduler configurado para usar 4 workers")
    
    print()

def compare_with_pandas_preview():
    """Comparación preliminar entre Pandas y Dask"""
    print("=" * 70)
    print("5. COMPARACIÓN PRELIMINAR: PANDAS vs DASK")
    print("=" * 70)
    
    n_rows = 500_000
    
    # Pandas
    print(f"\nProcesando {n_rows:,} filas con Pandas...")
    df_pandas = pd.DataFrame({
        'id': range(n_rows),
        'value': np.random.randn(n_rows),
        'category': np.random.choice(['A', 'B', 'C'], n_rows)
    })
    
    start = time.time()
    result_pandas = df_pandas.groupby('category')['value'].mean()
    time_pandas = time.time() - start
    print(f"Tiempo Pandas: {time_pandas:.4f} segundos")
    
    # Dask
    print(f"\nProcesando {n_rows:,} filas con Dask...")
    ddf = dd.from_pandas(df_pandas, npartitions=4)
    
    start = time.time()
    result_dask = ddf.groupby('category')['value'].mean().compute()
    time_dask = time.time() - start
    print(f"Tiempo Dask: {time_dask:.4f} segundos")
    
    print(f"\nResultados:")
    print(f"Pandas:\n{result_pandas}")
    print(f"Dask:\n{result_dask}")
    print(f"\nNota: Esta es una comparación preliminar con datos pequeños.")
    print("La ventaja de Dask se verá más claramente con datasets mayores a la RAM.")
    print()

def main():
    """Función principal"""
    print("\n" + "=" * 70)
    print("EXPLORACIÓN DE DASK - ENTREGA 2")
    print("Revisión del funcionamiento teórico de Dask")
    print("=" * 70 + "\n")
    
    # Asegurar que existe el directorio de resultados
    Path("results/figures").mkdir(parents=True, exist_ok=True)
    
    try:
        demonstrate_dask_arrays()
        demonstrate_dask_dataframes()
        demonstrate_lazy_evaluation()
        demonstrate_scheduler_info()
        compare_with_pandas_preview()
        
        print("=" * 70)
        print("EXPLORACIÓN COMPLETADA")
        print("=" * 70)
        print("\nConceptos clave demostrados:")
        print("1. ✓ Dask Arrays para procesamiento paralelo de arrays")
        print("2. ✓ Dask DataFrames para procesamiento paralelo de tablas")
        print("3. ✓ Evaluación diferida (lazy evaluation)")
        print("4. ✓ Scheduler y paralelismo")
        print("5. ✓ Comparación preliminar con Pandas")
        print("\n")
        
    except Exception as e:
        print(f"\n⚠ Error durante la ejecución: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

