# Entrega 4: Implementación con Pandas para Comparación

## Objetivo

Implementar las mismas tareas de procesamiento de datos usando Pandas y comparar el rendimiento con Dask.

## Archivos

### `compare_pandas_dask.py`
Script que realiza benchmarks comparativos:
- Lectura de datos
- Filtrado
- Agrupación (GroupBy)
- Agregaciones
- Medición de tiempo y memoria

**Uso:**
```bash
python entregas/entrega_4/compare_pandas_dask.py
```

## Métricas Medidas

1. **Tiempo de Ejecución**: Segundos que tarda cada operación
2. **Memoria Promedio**: Uso promedio de memoria durante la ejecución
3. **Memoria Pico**: Uso máximo de memoria
4. **Speedup**: Factor de aceleración (tiempos Pandas / tiempos Dask)

## Limitaciones de Pandas

Para datasets muy grandes (>2GB):
- Pandas puede fallar por falta de memoria
- Se usa una muestra para la comparación
- Esto demuestra la ventaja de Dask con datos grandes

## Resultados

Los resultados se guardan en:
- `data/processed/benchmark_results.csv`

Este archivo contiene todas las métricas medidas y se usa en la entrega 5 para visualización.

## Próximos Pasos

Ejecutar la entrega 5 para visualizar los resultados:
```bash
python entregas/entrega_5/visualize_results.py
```

