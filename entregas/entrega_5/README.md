# Entrega 5: Medición, Análisis y Visualización de Resultados

## Objetivo

Analizar y visualizar los resultados de la comparación entre Pandas y Dask, generando gráficos y reportes que demuestren las diferencias de rendimiento.

## Archivos

### `visualize_results.py`
Script que genera:
- Gráficos de comparación de tiempos
- Gráficos de comparación de memoria
- Análisis de speedup (aceleración)
- Tablas comparativas
- Reporte resumen en texto

**Uso:**
```bash
python entregas/entrega_5/visualize_results.py
```

## Requisitos Previos

1. Ejecutar primero la entrega 4 para generar los datos de benchmark:
```bash
python entregas/entrega_4/compare_pandas_dask.py
```

2. Esto generará `data/processed/benchmark_results.csv`

## Visualizaciones Generadas

### 1. Comparación de Tiempos
- Gráfico de barras comparando tiempos de ejecución
- Muestra qué método es más rápido para cada operación

### 2. Comparación de Memoria
- Gráfico de barras comparando uso de memoria
- Demuestra la eficiencia de Dask en manejo de memoria

### 3. Análisis de Speedup
- Muestra cuántas veces más rápido es Dask (o Pandas)
- Valores > 1 indican que Dask es más rápido

### 4. Tabla Comparativa
- Tabla completa con todos los resultados
- Incluye tiempos, memoria y métricas de comparación

### 5. Reporte Resumen
- Reporte en texto con conclusiones
- Estadísticas generales y análisis por operación

## Archivos de Salida

Todos los archivos se guardan en:
- `results/figures/` - Gráficos (PNG)
- `results/reports/` - Reportes (TXT)

## Interpretación de Resultados

### Speedup > 1
- Dask es más rápido para esa operación
- Ventaja clara de Dask

### Speedup < 1
- Pandas es más rápido
- Puede deberse a overhead de Dask en operaciones pequeñas

### Reducción de Memoria
- Porcentaje de memoria ahorrada usando Dask
- Valores positivos indican que Dask usa menos memoria

## Próximos Pasos

1. Revisar las visualizaciones generadas
2. Analizar los resultados
3. Preparar el informe final en formato IEEE (Entrega 6)

