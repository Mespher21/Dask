"""
Script para visualizar y analizar los resultados del experimento
Entrega 5: Medición, análisis y visualización de resultados
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path
import sys

# Agregar el directorio raíz al path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.config import PROCESSED_DATA_DIR, FIGURES_DIR, REPORTS_DIR

# Configurar estilo de gráficos
try:
    plt.style.use('seaborn-v0_8-darkgrid')
except:
    try:
        plt.style.use('seaborn-darkgrid')
    except:
        plt.style.use('ggplot')
sns.set_palette("husl")

def load_benchmark_results():
    """Carga los resultados del benchmark"""
    results_path = PROCESSED_DATA_DIR / "benchmark_results.csv"
    
    if not results_path.exists():
        print("⚠ No se encontraron resultados de benchmark")
        print("  Ejecuta primero: python entregas/entrega_4/compare_pandas_dask.py")
        return None
    
    return pd.read_csv(results_path)

def plot_time_comparison(results_df):
    """Gráfico de comparación de tiempos"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Preparar datos
    comparison = results_df.pivot(index='operation', columns='method', values='time')
    
    x = np.arange(len(comparison))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, comparison['Pandas'], width, label='Pandas', alpha=0.8)
    bars2 = ax.bar(x + width/2, comparison['Dask'], width, label='Dask', alpha=0.8)
    
    ax.set_xlabel('Operación', fontsize=12)
    ax.set_ylabel('Tiempo (segundos)', fontsize=12)
    ax.set_title('Comparación de Tiempos de Ejecución: Pandas vs Dask', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(comparison.index, rotation=45, ha='right')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    # Agregar valores en las barras
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.2f}s',
                   ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    output_path = FIGURES_DIR / "time_comparison.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✓ Gráfico guardado: {output_path}")
    plt.close()

def plot_memory_comparison(results_df):
    """Gráfico de comparación de memoria"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Preparar datos
    comparison = results_df.pivot(index='operation', columns='method', values='memory_avg')
    
    x = np.arange(len(comparison))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, comparison['Pandas'], width, label='Pandas', alpha=0.8)
    bars2 = ax.bar(x + width/2, comparison['Dask'], width, label='Dask', alpha=0.8)
    
    ax.set_xlabel('Operación', fontsize=12)
    ax.set_ylabel('Memoria Promedio (MB)', fontsize=12)
    ax.set_title('Comparación de Uso de Memoria: Pandas vs Dask', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(comparison.index, rotation=45, ha='right')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    # Agregar valores en las barras
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}MB',
                   ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    output_path = FIGURES_DIR / "memory_comparison.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✓ Gráfico guardado: {output_path}")
    plt.close()

def plot_speedup_analysis(results_df):
    """Análisis de speedup (aceleración)"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Calcular speedup
    comparison = results_df.pivot(index='operation', columns='method', values='time')
    speedup = comparison['Pandas'] / comparison['Dask']
    
    colors = ['green' if s > 1 else 'red' for s in speedup]
    bars = ax.bar(range(len(speedup)), speedup, color=colors, alpha=0.7)
    
    ax.axhline(y=1, color='black', linestyle='--', linewidth=1, label='Línea base (1x)')
    ax.set_xlabel('Operación', fontsize=12)
    ax.set_ylabel('Speedup (x veces más rápido)', fontsize=12)
    ax.set_title('Análisis de Speedup: Dask vs Pandas', fontsize=14, fontweight='bold')
    ax.set_xticks(range(len(speedup)))
    ax.set_xticklabels(speedup.index, rotation=45, ha='right')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    # Agregar valores
    for i, (bar, val) in enumerate(zip(bars, speedup)):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{val:.2f}x',
               ha='center', va='bottom' if val > 1 else 'top', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    output_path = FIGURES_DIR / "speedup_analysis.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✓ Gráfico guardado: {output_path}")
    plt.close()

def generate_summary_report(results_df):
    """Genera un reporte resumen en texto"""
    report_path = REPORTS_DIR / "summary_report.txt"
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("="*70 + "\n")
        f.write("REPORTE DE RESULTADOS: COMPARACIÓN PANDAS vs DASK\n")
        f.write("="*70 + "\n\n")
        
        f.write("RESUMEN EJECUTIVO\n")
        f.write("-"*70 + "\n\n")
        
        # Estadísticas generales
        pandas_times = results_df[results_df['method'] == 'Pandas']['time']
        dask_times = results_df[results_df['method'] == 'Dask']['time']
        
        f.write(f"Tiempo promedio Pandas: {pandas_times.mean():.2f} segundos\n")
        f.write(f"Tiempo promedio Dask: {dask_times.mean():.2f} segundos\n")
        f.write(f"Speedup promedio: {pandas_times.mean() / dask_times.mean():.2f}x\n\n")
        
        pandas_memory = results_df[results_df['method'] == 'Pandas']['memory_avg']
        dask_memory = results_df[results_df['method'] == 'Dask']['memory_avg']
        
        f.write(f"Memoria promedio Pandas: {pandas_memory.mean():.2f} MB\n")
        f.write(f"Memoria promedio Dask: {dask_memory.mean():.2f} MB\n")
        f.write(f"Reducción de memoria: {(1 - dask_memory.mean() / pandas_memory.mean()) * 100:.1f}%\n\n")
        
        f.write("="*70 + "\n")
        f.write("RESULTADOS POR OPERACIÓN\n")
        f.write("="*70 + "\n\n")
        
        # Resultados por operación
        for operation in results_df['operation'].unique():
            f.write(f"\n{operation.upper()}\n")
            f.write("-"*70 + "\n")
            
            op_data = results_df[results_df['operation'] == operation]
            
            for _, row in op_data.iterrows():
                f.write(f"{row['method']}:\n")
                f.write(f"  Tiempo: {row['time']:.2f} segundos\n")
                f.write(f"  Memoria: {row['memory_avg']:.2f} MB\n")
            
            # Comparación
            pandas_row = op_data[op_data['method'] == 'Pandas'].iloc[0]
            dask_row = op_data[op_data['method'] == 'Dask'].iloc[0]
            
            speedup = pandas_row['time'] / dask_row['time']
            memory_ratio = pandas_row['memory_avg'] / dask_row['memory_avg']
            
            f.write(f"\nComparación:\n")
            f.write(f"  Speedup: {speedup:.2f}x\n")
            f.write(f"  Reducción memoria: {(1 - 1/memory_ratio) * 100:.1f}%\n")
        
        f.write("\n" + "="*70 + "\n")
        f.write("CONCLUSIONES\n")
        f.write("="*70 + "\n\n")
        
        f.write("1. Dask muestra ventajas significativas en el manejo de datasets grandes\n")
        f.write("2. El uso de memoria es más eficiente con Dask debido al procesamiento por chunks\n")
        f.write("3. La velocidad depende del tipo de operación y tamaño del dataset\n")
        f.write("4. Para datasets pequeños, Pandas puede ser más rápido debido a overhead de Dask\n")
        f.write("5. Para datasets grandes (>1GB), Dask es la mejor opción\n")
    
    print(f"✓ Reporte guardado: {report_path}")

def create_comparison_table(results_df):
    """Crea una tabla comparativa"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.axis('tight')
    ax.axis('off')
    
    # Preparar datos para la tabla
    comparison = results_df.pivot(index='operation', columns='method', values=['time', 'memory_avg'])
    
    table_data = []
    for operation in comparison.index:
        pandas_time = comparison.loc[operation, ('time', 'Pandas')]
        dask_time = comparison.loc[operation, ('time', 'Dask')]
        pandas_mem = comparison.loc[operation, ('memory_avg', 'Pandas')]
        dask_mem = comparison.loc[operation, ('memory_avg', 'Dask')]
        
        speedup = pandas_time / dask_time
        mem_reduction = (1 - dask_mem / pandas_mem) * 100
        
        table_data.append([
            operation,
            f"{pandas_time:.2f}s",
            f"{dask_time:.2f}s",
            f"{speedup:.2f}x",
            f"{pandas_mem:.1f}MB",
            f"{dask_mem:.1f}MB",
            f"{mem_reduction:.1f}%"
        ])
    
    headers = ['Operación', 'Pandas\nTiempo', 'Dask\nTiempo', 'Speedup', 
               'Pandas\nMemoria', 'Dask\nMemoria', 'Reducción\nMemoria']
    
    table = ax.table(cellText=table_data, colLabels=headers,
                    cellLoc='center', loc='center',
                    colWidths=[0.2, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12])
    
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 2)
    
    # Colorear filas
    for i in range(len(table_data)):
        if i % 2 == 0:
            for j in range(len(headers)):
                table[(i+1, j)].set_facecolor('#f0f0f0')
    
    plt.title('Tabla Comparativa: Pandas vs Dask', fontsize=16, fontweight='bold', pad=20)
    
    output_path = FIGURES_DIR / "comparison_table.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✓ Tabla guardada: {output_path}")
    plt.close()

def main():
    """Función principal"""
    print("\n" + "="*70)
    print("ENTREGA 5: VISUALIZACIÓN Y ANÁLISIS DE RESULTADOS")
    print("="*70 + "\n")
    
    # Asegurar que existen los directorios
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Cargar resultados
    results_df = load_benchmark_results()
    
    if results_df is None:
        return
    
    print(f"Resultados cargados: {len(results_df)} registros")
    print(f"Operaciones: {results_df['operation'].unique()}\n")
    
    # Generar visualizaciones
    print("Generando visualizaciones...")
    plot_time_comparison(results_df)
    plot_memory_comparison(results_df)
    plot_speedup_analysis(results_df)
    create_comparison_table(results_df)
    
    # Generar reporte
    print("\nGenerando reporte...")
    generate_summary_report(results_df)
    
    print("\n" + "="*70)
    print("VISUALIZACIÓN COMPLETADA")
    print("="*70)
    print("\nArchivos generados:")
    print(f"  - {FIGURES_DIR}/time_comparison.png")
    print(f"  - {FIGURES_DIR}/memory_comparison.png")
    print(f"  - {FIGURES_DIR}/speedup_analysis.png")
    print(f"  - {FIGURES_DIR}/comparison_table.png")
    print(f"  - {REPORTS_DIR}/summary_report.txt")
    print("\n✓ Proceso completado\n")

if __name__ == "__main__":
    main()

