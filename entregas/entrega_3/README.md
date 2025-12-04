# Entrega 3: Lectura y Primeras Transformaciones con Dask

## Objetivo

Implementar la lectura de datasets grandes y realizar transformaciones básicas usando Dask, demostrando su capacidad para manejar datos que no caben en memoria.

## Archivos

### `read_data_dask.py`
Script que demuestra:
- Lectura de archivos CSV grandes con Dask
- Comparación de tiempos de lectura con Pandas
- Manejo de memoria eficiente
- Particionado automático de datos

**Uso:**
```bash
python entregas/entrega_3/read_data_dask.py
```

### `transform_data_dask.py`
Script que implementa:
- Limpieza de datos (eliminación de duplicados, valores nulos)
- Filtrado de datos
- Transformaciones (tipos de datos, columnas derivadas)
- Agregaciones (groupby, estadísticas)
- Guardado de datos procesados

**Uso:**
```bash
python entregas/entrega_3/transform_data_dask.py
```

## Requisitos

1. **Dataset**: Un archivo CSV de al menos 1 GB en `data/raw/`

2. **Dependencias**: Instaladas con `pip install -r requirements.txt`

## Pipeline de Procesamiento

```
1. Lectura → 2. Limpieza → 3. Filtrado → 4. Transformaciones → 5. Agregaciones → 6. Guardado
```

### 1. Lectura
- Dask lee el archivo en chunks (particiones)
- No carga todo en memoria de una vez
- Permite procesar archivos mayores que la RAM disponible

### 2. Limpieza
- Eliminación de filas duplicadas
- Manejo de valores nulos
- Optimización de tipos de datos

### 3. Filtrado
- Aplicación de condiciones de filtrado
- Reducción del tamaño del dataset

### 4. Transformaciones
- Conversión de tipos de datos
- Creación de columnas derivadas
- Normalización de datos

### 5. Agregaciones
- Operaciones groupby
- Cálculo de estadísticas
- Resúmenes de datos

### 6. Guardado
- Exportación a formato Parquet (eficiente)
- Preparación para análisis posterior

## Ventajas de Dask en esta Entrega

1. **Memoria**: No requiere cargar todo el dataset en RAM
2. **Velocidad**: Procesamiento paralelo de particiones
3. **Escalabilidad**: Puede manejar datasets de cualquier tamaño
4. **API Familiar**: Similar a Pandas, fácil de usar

## Comparación con Pandas

| Característica | Pandas | Dask |
|---------------|--------|------|
| Tamaño máximo | Limitado por RAM | Ilimitado |
| Velocidad lectura | Rápida (si cabe en RAM) | Rápida (chunks) |
| Memoria | Todo en RAM | Solo chunks activos |
| Paralelismo | No nativo | Sí (múltiples cores) |

## Ejemplo de Uso

```python
# Leer dataset grande
ddf = dd.read_csv('data/raw/large_dataset.csv', blocksize='100MB')

# Limpiar datos
ddf_clean = ddf.drop_duplicates()

# Filtrar
ddf_filtered = ddf_clean[ddf_clean['valor'] > 0]

# Transformar
ddf_transformed = ddf_filtered.assign(
    nuevo_campo = ddf_filtered['campo1'] * 2
)

# Agregar
resultado = ddf_transformed.groupby('categoria')['valor'].mean().compute()

# Guardar
ddf_transformed.to_parquet('data/processed/resultado.parquet')
```

## Próximos Pasos

1. **Entrega 4**: Implementar las mismas operaciones con Pandas
2. **Entrega 5**: Comparar rendimiento y generar visualizaciones

## Notas

- Ajusta los filtros y transformaciones según tu dataset específico
- El formato Parquet es más eficiente que CSV para datos procesados
- Los tiempos de ejecución pueden variar según el hardware

