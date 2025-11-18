# Uso de Dask para el Análisis Paralelo y Escalable de Datos Masivos en Python

## Descripción del Proyecto

Este proyecto evalúa el rendimiento y la escalabilidad de Dask en el análisis de datos masivos, comparándolo con Pandas para identificar sus ventajas, desventajas y posibles aplicaciones prácticas.

## Objetivos

### Objetivo General
Evaluar el rendimiento y la escalabilidad de Dask en el análisis de datos masivos, comparándolo con Pandas.

### Objetivos Específicos
1. Analizar el funcionamiento interno de Dask (modelo de tareas, scheduler, paralelismo y ejecución diferida)
2. Seleccionar un dataset mayor a 1 GB y preparar un entorno de experimentación
3. Implementar tareas típicas de procesamiento de datos: lectura, limpieza, filtros, transformaciones, agregaciones y combinaciones
4. Comparar tiempos de ejecución, uso de memoria y eficiencia entre Pandas y Dask
5. Visualizar y documentar los resultados del experimento
6. Elaborar un informe final bajo formato IEEE
7. Crear un repositorio en GitHub con el código, instrucciones y resultados

## Estructura del Proyecto

```
Dask/
├── entregas/              # Código organizado por entregas
│   ├── entrega_1/        # Selección de dataset y diseño del experimento
│   ├── entrega_2/        # Revisión del funcionamiento teórico de Dask
│   ├── entrega_3/        # Lectura y primeras transformaciones con Dask
│   ├── entrega_4/        # Implementación con Pandas para comparación
│   ├── entrega_5/        # Medición, análisis y visualización de resultados
│   └── entrega_6/        # Ajustes finales y documentación
├── data/                 # Datasets (no incluidos en git)
│   ├── raw/              # Datos originales
│   └── processed/        # Datos procesados
├── results/              # Resultados de experimentos
│   ├── figures/          # Gráficos y visualizaciones
│   └── reports/          # Reportes y métricas
├── src/                  # Código fuente reutilizable
│   ├── utils/            # Utilidades y helpers
│   └── benchmarks/       # Scripts de benchmarking
├── docs/                 # Documentación adicional
└── requirements.txt      # Dependencias del proyecto
```

## Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd Dask
```

2. Crear un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### Entrega 2: Configuración Inicial y Selección de Dataset

Ejecutar el script de configuración inicial:
```bash
python entregas/entrega_2/setup_dataset.py
```

## Plan de Trabajo

- **Semana 1**: Selección del dataset y diseño del experimento
- **Semana 2**: Revisión del funcionamiento teórico de Dask
- **Semana 3**: Lectura y primeras transformaciones con Dask
- **Semana 4**: Implementación de las mismas tareas con Pandas para comparación
- **Semana 5**: Medición, análisis y visualización de resultados
- **Semana 6**: Redacción del informe técnico en formato IEEE
- **Semana 7**: Ajustes finales, documentación y preparación del repositorio

## Requisitos

- Python 3.8+
- Dask
- Pandas
- NumPy
- Matplotlib/Seaborn (para visualizaciones)

Ver `requirements.txt` para la lista completa de dependencias.

## Autor

[Mauro Espinoza]

## Licencia

Este proyecto es parte de un trabajo académico.

