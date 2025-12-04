"""
Script para realizar transformaciones y limpieza de datos con Dask
Entrega 3: Lectura y primeras transformaciones con Dask
"""

import sys

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
from pathlib import Path

# Agregar el directorio raíz al path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.config import RAW_DATA_DIR, PROCESSED_DATA_DIR, get_data_path

def clean_data(ddf):
    """
    Realiza limpieza básica de datos
    
    Parameters:
    -----------
    ddf : dask.DataFrame
        DataFrame de Dask a limpiar
    """
    print(f"\n{'='*70}")
    print("LIMPIEZA DE DATOS")
    print(f"{'='*70}")
    
    original_shape = (len(ddf), len(ddf.columns))
    print(f"\nForma original: {original_shape[0]:,} filas x {original_shape[1]} columnas")
    
    start_time = time.time()
    
    # 1. Eliminar filas duplicadas
    print("\n1. Eliminando filas duplicadas...")
    ddf_clean = ddf.drop_duplicates()
    n_duplicates = original_shape[0] - len(ddf_clean)
    print(f"   Filas duplicadas encontradas: {n_duplicates:,}")
    
    # 2. Eliminar columnas completamente nulas
    print("\n2. Verificando columnas completamente nulas...")
    null_counts = ddf_clean.isnull().sum().compute()
    completely_null = null_counts[null_counts == len(ddf_clean)]
    if len(completely_null) > 0:
        print(f"   Columnas completamente nulas: {list(completely_null.index)}")
        ddf_clean = ddf_clean.drop(columns=completely_null.index)
    else:
        print("   No hay columnas completamente nulas")
    
    # 3. Información sobre valores nulos
    print("\n3. Análisis de valores nulos por columna:")
    null_info = null_counts[null_counts > 0].sort_values(ascending=False)
    if len(null_info) > 0:
        for col, count in null_info.head(10).items():
            pct = (count / len(ddf_clean)) * 100
            print(f"   {col}: {count:,} ({pct:.1f}%)")
    else:
        print("   No hay valores nulos")
    
    clean_time = time.time() - start_time
    final_shape = (len(ddf_clean), len(ddf_clean.columns))
    
    print(f"\n✓ Limpieza completada en {clean_time:.2f} segundos")
    print(f"Forma final: {final_shape[0]:,} filas x {final_shape[1]} columnas")
    print(f"Filas eliminadas: {original_shape[0] - final_shape[0]:,}")
    
    return ddf_clean

def filter_data(ddf, filters=None):
    """
    Aplica filtros al DataFrame
    
    Parameters:
    -----------
    ddf : dask.DataFrame
        DataFrame de Dask
    filters : dict
        Diccionario con filtros a aplicar {columna: condición}
    """
    print(f"\n{'='*70}")
    print("FILTRADO DE DATOS")
    print(f"{'='*70}")
    
    if filters is None:
        print("\n⚠ No se especificaron filtros")
        print("  Ejemplo de uso:")
        print("    filters = {'columna1': lambda x: x > 100}")
        return ddf
    
    original_count = len(ddf)
    print(f"\nFilas antes del filtrado: {original_count:,}")
    
    start_time = time.time()
    
    ddf_filtered = ddf.copy()
    for col, condition in filters.items():
        if col in ddf_filtered.columns:
            print(f"\nAplicando filtro en '{col}'...")
            if callable(condition):
                ddf_filtered = ddf_filtered[condition(ddf_filtered[col])]
            else:
                ddf_filtered = ddf_filtered[ddf_filtered[col] == condition]
            
            filtered_count = len(ddf_filtered)
            print(f"  Filas después del filtro: {filtered_count:,}")
            print(f"  Filas eliminadas: {original_count - filtered_count:,}")
            original_count = filtered_count
        else:
            print(f"  ⚠ Columna '{col}' no encontrada")
    
    filter_time = time.time() - start_time
    final_count = len(ddf_filtered)
    
    print(f"\n✓ Filtrado completado en {filter_time:.2f} segundos")
    print(f"Filas finales: {final_count:,}")
    print(f"Reducción: {((original_count - final_count) / original_count * 100):.1f}%")
    
    return ddf_filtered

def transform_data(ddf):
    """
    Realiza transformaciones en los datos
    
    Parameters:
    -----------
    ddf : dask.DataFrame
        DataFrame de Dask
    """
    print(f"\n{'='*70}")
    print("TRANSFORMACIONES DE DATOS")
    print(f"{'='*70}")
    
    start_time = time.time()
    ddf_transformed = ddf.copy()
    
    # 1. Convertir tipos de datos
    print("\n1. Optimizando tipos de datos...")
    for col in ddf_transformed.columns:
        col_dtype = ddf_transformed[col].dtype
        
        # Intentar convertir a tipos más eficientes
        if col_dtype == 'object':
            # Intentar convertir a categoría si tiene pocos valores únicos
            try:
                n_unique = ddf_transformed[col].nunique().compute()
                if n_unique < len(ddf_transformed) * 0.5:  # Menos del 50% valores únicos
                    ddf_transformed[col] = ddf_transformed[col].astype('category')
                    print(f"   {col}: object -> category ({n_unique} valores únicos)")
            except:
                pass
        
        elif col_dtype in ['int64', 'float64']:
            # Intentar downcast
            try:
                if col_dtype == 'int64':
                    ddf_transformed[col] = dd.to_numeric(ddf_transformed[col], downcast='integer')
                elif col_dtype == 'float64':
                    ddf_transformed[col] = dd.to_numeric(ddf_transformed[col], downcast='float')
            except:
                pass
    
    # 2. Crear nuevas columnas derivadas (ejemplos)
    print("\n2. Creando columnas derivadas (ejemplos)...")
    
    # Buscar columnas numéricas para operaciones
    numeric_cols = ddf_transformed.select_dtypes(include=[np.number]).columns.tolist()
    
    if len(numeric_cols) >= 2:
        # Suma de primeras dos columnas numéricas
        col1, col2 = numeric_cols[0], numeric_cols[1]
        # Asegurar que el resultado sea float64 para evitar problemas de overflow
        ddf_transformed[f'{col1}_plus_{col2}'] = (
            ddf_transformed[col1].astype('float64') + 
            ddf_transformed[col2].astype('float64')
        )
        print(f"   Creada columna: {col1}_plus_{col2} (float64)")
    
    if len(numeric_cols) >= 1:
        # Cuadrado de primera columna numérica
        col = numeric_cols[0]
        # Usar int64 para evitar overflow (int8 solo va hasta 127)
        if ddf_transformed[col].dtype in ['int8', 'int16', 'int32']:
            ddf_transformed[f'{col}_squared'] = (
                ddf_transformed[col].astype('int64') ** 2
            ).astype('int64')
        else:
            # Para float, mantener como float64
            ddf_transformed[f'{col}_squared'] = (
                ddf_transformed[col].astype('float64') ** 2
            ).astype('float64')
        print(f"   Creada columna: {col}_squared")
    
    transform_time = time.time() - start_time
    
    print(f"\n✓ Transformaciones completadas en {transform_time:.2f} segundos")
    print(f"Columnas finales: {len(ddf_transformed.columns)}")
    
    return ddf_transformed

def aggregate_data(ddf, groupby_col=None, agg_cols=None):
    """
    Realiza agregaciones en los datos
    
    Parameters:
    -----------
    ddf : dask.DataFrame
        DataFrame de Dask
    groupby_col : str
        Columna por la cual agrupar
    agg_cols : dict
        Diccionario con columnas y funciones de agregación
    """
    print(f"\n{'='*70}")
    print("AGREGACIONES DE DATOS")
    print(f"{'='*70}")
    
    if groupby_col is None or groupby_col not in ddf.columns:
        print("\n⚠ No se especificó columna de agrupación válida")
        print("  Mostrando estadísticas descriptivas generales...")
        
        numeric_cols = ddf.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            print("\nEstadísticas descriptivas:")
            stats = ddf[numeric_cols].describe().compute()
            print(stats)
        return None
    
    start_time = time.time()
    
    print(f"\nAgrupando por: {groupby_col}")
    
    if agg_cols is None:
        # Agregaciones por defecto en columnas numéricas
        numeric_cols = ddf.select_dtypes(include=[np.number]).columns.tolist()
        if groupby_col in numeric_cols:
            numeric_cols.remove(groupby_col)
        
        if len(numeric_cols) > 0:
            agg_cols = {col: ['mean', 'sum', 'count'] for col in numeric_cols[:3]}  # Primeras 3
    
    print(f"Agregaciones: {agg_cols}")
    
    # Realizar agregación
    grouped = ddf.groupby(groupby_col).agg(agg_cols).compute()
    
    agg_time = time.time() - start_time
    
    print(f"\n✓ Agregación completada en {agg_time:.2f} segundos")
    print(f"\nResultado:")
    print(grouped.head(10))
    
    return grouped

def normalize_dtypes(ddf):
    """
    Normaliza los tipos de datos para evitar problemas al guardar en Parquet
    
    Parameters:
    -----------
    ddf : dask.DataFrame
        DataFrame de Dask
    """
    print("\nNormalizando tipos de datos para Parquet...")
    ddf_normalized = ddf.copy()
    
    for col in ddf_normalized.columns:
        col_dtype = str(ddf_normalized[col].dtype)
        
        # Normalizar tipos enteros
        if 'int' in col_dtype:
            # Para columnas que terminan en _squared, usar int64 (valores grandes)
            if col.endswith('_squared'):
                ddf_normalized[col] = ddf_normalized[col].astype('int64')
                print(f"   {col}: {col_dtype} -> int64 (columna derivada)")
            # Para IDs y otras columnas enteras, usar int32 (más seguro que int8)
            elif col == 'id' or 'id' in col.lower():
                ddf_normalized[col] = ddf_normalized[col].astype('int32')
                print(f"   {col}: {col_dtype} -> int32")
            else:
                # Para otras columnas enteras, usar int32 por defecto
                # int8 solo va de -128 a 127, muy limitado
                if 'int8' in col_dtype or 'int16' in col_dtype:
                    ddf_normalized[col] = ddf_normalized[col].astype('int32')
                    print(f"   {col}: {col_dtype} -> int32")
                # Si ya es int32 o int64, mantenerlo
                elif 'int32' in col_dtype:
                    pass  # Ya es int32
                elif 'int64' in col_dtype:
                    pass  # Mantener int64 si es necesario
        
        # Normalizar tipos flotantes
        elif 'float' in col_dtype:
            # Para columnas derivadas con _plus_, usar float64
            if '_plus_' in col:
                ddf_normalized[col] = ddf_normalized[col].astype('float64')
                print(f"   {col}: {col_dtype} -> float64 (columna derivada)")
            # Para otras, mantener float64 (más seguro)
            elif 'float32' in col_dtype:
                # Convertir float32 a float64 para evitar problemas
                ddf_normalized[col] = ddf_normalized[col].astype('float64')
                print(f"   {col}: {col_dtype} -> float64")
            # Si ya es float64, mantenerlo
            else:
                pass
        
        # Normalizar strings y categorías
        elif col_dtype == 'object' or 'category' in col_dtype:
            # Mantener como está, PyArrow manejará strings
            pass
    
    print("✓ Normalización de tipos completada")
    return ddf_normalized

def save_processed_data(ddf, filename='processed_data.parquet'):
    """
    Guarda el DataFrame procesado
    
    Parameters:
    -----------
    ddf : dask.DataFrame
        DataFrame de Dask procesado
    filename : str
        Nombre del archivo de salida
    """
    print(f"\n{'='*70}")
    print("GUARDANDO DATOS PROCESADOS")
    print(f"{'='*70}")
    
    output_path = PROCESSED_DATA_DIR / filename
    
    print(f"\nGuardando en: {output_path}")
    print("Formato: Parquet (eficiente para Dask)")
    
    start_time = time.time()
    
    # Normalizar tipos antes de guardar
    ddf_normalized = normalize_dtypes(ddf)
    
    # Guardar en formato Parquet (más eficiente que CSV)
    try:
        print("Intentando guardar con PyArrow...")
        ddf_normalized.to_parquet(
            str(output_path),
            write_index=False,
            engine='pyarrow'
        )
    except Exception as e:
        # Si falla, intentar con fastparquet
        print(f"\n⚠ Error con PyArrow: {str(e)[:200]}")
        print("Intentando con fastparquet...")
        try:
            ddf_normalized.to_parquet(
                str(output_path),
                write_index=False,
                engine='fastparquet'
            )
        except Exception as e2:
            # Si todo falla, guardar como CSV
            print(f"\n⚠ Error al guardar en Parquet con ambos engines")
            print(f"   PyArrow: {str(e)[:200]}")
            print(f"   FastParquet: {str(e2)[:200]}")
            print("\nGuardando como CSV (más lento pero más compatible)...")
            csv_path = output_path.with_suffix('.csv')
            try:
                ddf_normalized.to_csv(csv_path, index=False, single_file=True)
                print(f"✓ Guardado como CSV en: {csv_path}")
            except Exception as e3:
                print(f"\n✗ Error crítico al guardar: {str(e3)[:200]}")
                raise
            return
    
    save_time = time.time() - start_time
    
    file_size = output_path.stat().st_size / (1024**2)  # MB
    print(f"\n✓ Datos guardados en {save_time:.2f} segundos")
    print(f"Tamaño del archivo: {file_size:.2f} MB")
    print(f"Ubicación: {output_path}")

def find_data_files():
    """
    Busca archivos de datos disponibles (CSV o Parquet)
    Retorna el archivo más apropiado para procesar
    """
    # Buscar CSV en raw/
    csv_files = list(RAW_DATA_DIR.glob("*.csv")) if RAW_DATA_DIR.exists() else []
    
    # Buscar Parquet en processed/ (puede estar en subdirectorio)
    parquet_files = []
    if PROCESSED_DATA_DIR.exists():
        # Buscar archivos .parquet directamente
        parquet_files = list(PROCESSED_DATA_DIR.glob("*.parquet"))
        
        # Buscar en subdirectorios también (Dask a veces crea subdirs)
        parquet_dirs = [d for d in PROCESSED_DATA_DIR.iterdir() if d.is_dir()]
        for parquet_dir in parquet_dirs:
            # Buscar archivos .parquet en el subdirectorio
            parquet_in_dir = list(parquet_dir.glob("*.parquet"))
            if parquet_in_dir:
                # Si hay archivos .parquet, el directorio es un dataset
                parquet_files.append(parquet_dir)
            else:
                # Buscar archivos _metadata o _common_metadata (indicadores de dataset Parquet)
                metadata_files = list(parquet_dir.glob("*_metadata"))
                if metadata_files:
                    parquet_files.append(parquet_dir)  # El directorio completo es el dataset
    
    return csv_files, parquet_files

def main():
    """Función principal"""
    print("\n" + "="*70)
    print("ENTREGA 3: TRANSFORMACIONES Y LIMPIEZA DE DATOS CON DASK")
    print("="*70 + "\n")
    
    # Buscar archivos de datos
    csv_files, parquet_files = find_data_files()
    
    # Mostrar archivos encontrados
    print("Buscando archivos de datos...")
    if csv_files:
        print(f"  ✓ Encontrados {len(csv_files)} archivo(s) CSV en data/raw/")
        for f in csv_files[:3]:  # Mostrar máximo 3
            print(f"    - {f.name}")
    if parquet_files:
        print(f"  ✓ Encontrados {len(parquet_files)} archivo(s) Parquet en data/processed/")
        for f in parquet_files[:3]:  # Mostrar máximo 3
            if f.is_dir():
                print(f"    - {f.name}/ (directorio)")
            else:
                print(f"    - {f.name}")
    
    # Decidir qué archivo usar
    # Prioridad: 1) CSV en raw/ (datos originales), 2) Parquet en processed/ (si ya procesado)
    ddf = None
    file_used = None
    
    if len(csv_files) > 0:
        # Usar CSV de raw/ (datos originales)
        file_used = csv_files[0]
        print(f"\n📂 Leyendo archivo CSV: {file_used.name}")
        print(f"   Ubicación: {file_used}")
        try:
            ddf = dd.read_csv(str(file_used), blocksize='100MB')
        except Exception as e:
            print(f"\n✗ Error al leer CSV: {str(e)[:200]}")
            print("   Intentando con Parquet...")
            if len(parquet_files) > 0:
                file_used = parquet_files[0]
                print(f"\n📂 Leyendo archivo Parquet: {file_used.name if not file_used.is_dir() else file_used}")
                try:
                    ddf = dd.read_parquet(str(file_used))
                except Exception as e2:
                    print(f"\n✗ Error al leer Parquet: {str(e2)[:200]}")
                    print("\n⚠ No se pudo leer ningún archivo")
                    return
            else:
                print("\n⚠ No hay archivos Parquet disponibles")
                return
    elif len(parquet_files) > 0:
        # Usar Parquet si no hay CSV
        file_used = parquet_files[0]
        print(f"\n📂 Leyendo archivo Parquet: {file_used.name if not file_used.is_dir() else file_used}")
        print(f"   Ubicación: {file_used}")
        try:
            ddf = dd.read_parquet(str(file_used))
        except Exception as e:
            print(f"\n✗ Error al leer Parquet: {str(e)[:200]}")
            print("\n⚠ No se pudo leer el archivo Parquet")
            print("   Intenta ejecutar primero: python entregas/entrega_3/read_data_dask.py")
            return
    else:
        print("\n⚠ No se encontraron archivos de datos")
        print("\nOpciones:")
        print("1. Ejecutar primero: python entregas/entrega_3/read_data_dask.py")
        print("2. Colocar un archivo CSV en: data/raw/")
        print("3. Generar datos sintéticos: python entregas/entrega_3/generate_sample_data.py")
        return
    
    if ddf is None:
        print("\n✗ No se pudo cargar ningún archivo")
        return
    
    # Mostrar información del dataset cargado
    print(f"\n✓ Archivo cargado exitosamente")
    print(f"   Filas: {len(ddf):,}")
    print(f"   Columnas: {len(ddf.columns)}")
    cols_preview = list(ddf.columns)[:10]
    if len(ddf.columns) > 10:
        print(f"   Columnas: {cols_preview} ... (+{len(ddf.columns) - 10} más)")
    else:
        print(f"   Columnas: {cols_preview}")
    
    # Pipeline de procesamiento
    print("\n" + "="*70)
    print("INICIANDO PIPELINE DE PROCESAMIENTO")
    print("="*70)
    
    # 1. Limpieza
    ddf_clean = clean_data(ddf)
    
    # 2. Filtrado (ejemplo - ajustar según tu dataset)
    # ddf_filtered = filter_data(ddf_clean, filters={
    #     'columna_numerica': lambda x: x > 0
    # })
    ddf_filtered = ddf_clean  # Sin filtros por ahora
    
    # 3. Transformaciones
    ddf_transformed = transform_data(ddf_filtered)
    
    # 4. Agregaciones (ejemplo - ajustar según tu dataset)
    # Buscar columna categórica para agrupar
    categorical_cols = ddf_transformed.select_dtypes(include=['object', 'category']).columns
    if len(categorical_cols) > 0:
        groupby_col = categorical_cols[0]
        aggregate_data(ddf_transformed, groupby_col=groupby_col)
    
    # 5. Guardar datos procesados
    save_processed_data(ddf_transformed, 'processed_data.parquet')
    
    print("\n" + "="*70)
    print("PIPELINE COMPLETADO")
    print("="*70)
    print("\nPróximos pasos:")
    print("  - Ejecutar: python entregas/entrega_4/compare_pandas_dask.py")
    print("  - Para comparar rendimiento con Pandas\n")

if __name__ == "__main__":
    main()

