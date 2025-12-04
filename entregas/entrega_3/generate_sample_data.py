"""
Script para generar datos sintéticos de prueba
Útil cuando no tienes un dataset real disponible
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Agregar el directorio raíz al path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.config import RAW_DATA_DIR

def generate_large_dataset(n_rows=2_000_000, output_file='sample_dataset.csv'):
    """
    Genera un dataset sintético grande para pruebas
    
    Parameters:
    -----------
    n_rows : int
        Número de filas a generar
    output_file : str
        Nombre del archivo de salida
    """
    print(f"\n{'='*70}")
    print("GENERACIÓN DE DATASET SINTÉTICO")
    print(f"{'='*70}")
    
    print(f"\nGenerando {n_rows:,} filas...")
    print("Esto puede tardar unos minutos...")
    
    # Generar datos en chunks para no saturar memoria
    chunk_size = 100_000
    chunks = []
    
    for i in range(0, n_rows, chunk_size):
        current_chunk_size = min(chunk_size, n_rows - i)
        
        chunk = pd.DataFrame({
            'id': range(i, i + current_chunk_size),
            'timestamp': pd.date_range('2020-01-01', periods=current_chunk_size, freq='1min'),
            'category': np.random.choice(['A', 'B', 'C', 'D', 'E'], current_chunk_size),
            'value1': np.random.randn(current_chunk_size) * 100,
            'value2': np.random.randn(current_chunk_size) * 50,
            'value3': np.random.uniform(0, 1000, current_chunk_size),
            'status': np.random.choice(['active', 'inactive', 'pending'], current_chunk_size),
            'score': np.random.uniform(0, 100, current_chunk_size),
            'region': np.random.choice(['North', 'South', 'East', 'West'], current_chunk_size),
            'amount': np.random.uniform(10, 10000, current_chunk_size)
        })
        
        chunks.append(chunk)
        
        if (i // chunk_size + 1) % 10 == 0:
            print(f"  Procesadas {i + current_chunk_size:,} filas...")
    
    # Combinar chunks
    print("\nCombinando chunks...")
    df = pd.concat(chunks, ignore_index=True)
    
    # Guardar
    output_path = RAW_DATA_DIR / output_file
    print(f"\nGuardando en: {output_path}")
    print("Esto puede tardar varios minutos...")
    
    df.to_csv(output_path, index=False)
    
    file_size_mb = output_path.stat().st_size / (1024**2)
    file_size_gb = file_size_mb / 1024
    
    print(f"\n✓ Dataset generado exitosamente")
    print(f"  Filas: {len(df):,}")
    print(f"  Columnas: {len(df.columns)}")
    print(f"  Tamaño: {file_size_mb:.2f} MB ({file_size_gb:.2f} GB)")
    print(f"  Ubicación: {output_path}")
    
    print("\n" + "="*70)
    print("DATASET LISTO PARA USAR")
    print("="*70)
    print("\nAhora puedes ejecutar:")
    print("  python entregas/entrega_3/read_data_dask.py")
    print()

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Genera un dataset sintético para pruebas')
    parser.add_argument('--rows', type=int, default=2_000_000,
                       help='Número de filas a generar (default: 2,000,000)')
    parser.add_argument('--output', type=str, default='sample_dataset.csv',
                       help='Nombre del archivo de salida (default: sample_dataset.csv)')
    
    args = parser.parse_args()
    
    # Asegurar que existe el directorio
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    generate_large_dataset(n_rows=args.rows, output_file=args.output)

