# Entrega 2: Revisión del Funcionamiento Teórico de Dask

## Objetivo

Revisar y comprender el funcionamiento interno de Dask, incluyendo:
- Modelo de tareas
- Scheduler
- Paralelismo
- Ejecución diferida (lazy evaluation)

## Archivos

### `setup_dataset.py`
Script de configuración inicial que:
- Crea la estructura de directorios del proyecto
- Verifica que las dependencias estén instaladas
- Proporciona información sobre datasets recomendados

**Uso:**
```bash
python entregas/entrega_2/setup_dataset.py
```

### `explore_dask.py`
Script de exploración que demuestra:
1. **Dask Arrays**: Procesamiento paralelo de arrays NumPy
2. **Dask DataFrames**: Procesamiento paralelo de DataFrames similares a Pandas
3. **Evaluación Diferida**: Cómo Dask construye grafos de tareas
4. **Scheduler**: Diferentes modos de ejecución
5. **Comparación Preliminar**: Primera comparación con Pandas

**Uso:**
```bash
python entregas/entrega_2/explore_dask.py
```

## Conceptos Clave

### 1. Modelo de Tareas
Dask construye un grafo acíclico dirigido (DAG) de tareas antes de ejecutarlas. Esto permite:
- Optimización de operaciones
- Paralelización automática
- Manejo eficiente de memoria

### 2. Scheduler
Dask puede usar diferentes schedulers:
- **Threaded**: Para operaciones con GIL liberado (I/O, NumPy)
- **Processes**: Para paralelismo verdadero (CPU-bound)
- **Distributed**: Para clústeres y escalabilidad

### 3. Chunks (Bloques)
Los datos se dividen en chunks (bloques) que pueden procesarse en paralelo:
```python
# Array dividido en chunks de 1000x1000
x = da.random.random((10000, 10000), chunks=(1000, 1000))
```

### 4. Lazy Evaluation
Las operaciones no se ejecutan inmediatamente, sino que se construyen como un grafo:
```python
result = (x + y) ** 2  # No se ejecuta aún
computed = result.compute()  # Ahora sí se ejecuta
```

## Próximos Pasos

1. Descargar un dataset de al menos 1 GB
2. Colocarlo en `data/raw/`
3. Probar la lectura del dataset con Dask
4. Comparar tiempos de lectura con Pandas

## Referencias

- [Documentación oficial de Dask](https://docs.dask.org/)
- [Dask Arrays](https://docs.dask.org/en/stable/array.html)
- [Dask DataFrames](https://docs.dask.org/en/stable/dataframe.html)
- [Schedulers de Dask](https://docs.dask.org/en/stable/scheduling.html)

