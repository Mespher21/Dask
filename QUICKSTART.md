# Guía de Inicio Rápido

## Pasos Iniciales

### 1. Configuración del Entorno

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Configuración Inicial del Proyecto

Ejecuta el script de configuración para crear la estructura de directorios:

```bash
python entregas/entrega_2/setup_dataset.py
```

Este script:
- ✓ Crea todos los directorios necesarios
- ✓ Verifica que las dependencias estén instaladas
- ✓ Muestra información sobre datasets recomendados

### 3. Explorar Dask

Ejecuta el script de exploración para entender cómo funciona Dask:

```bash
python entregas/entrega_2/explore_dask.py
```

Este script demuestra:
- Dask Arrays y DataFrames
- Evaluación diferida (lazy evaluation)
- Scheduler y paralelismo
- Comparación preliminar con Pandas

### 4. Descargar un Dataset

Necesitas un dataset de al menos 1 GB. Opciones recomendadas:

**Kaggle:**
- NYC Taxi Trip Data
- Amazon Product Reviews
- Google Play Store Apps

**ERA5 Climate Data:**
- Datos climáticos reanálisis
- https://cds.climate.copernicus.eu/

Coloca el dataset descargado en: `data/raw/`

### 5. Próximos Pasos

Una vez que tengas el dataset:

1. **Entrega 3**: Lectura y primeras transformaciones con Dask
2. **Entrega 4**: Implementación equivalente con Pandas
3. **Entrega 5**: Comparación de rendimiento y visualización

## Estructura del Proyecto

```
Dask/
├── entregas/              # Código por entregas
│   └── entrega_2/        # ← Estás aquí
├── data/                  # Datasets
│   ├── raw/              # Datos originales
│   └── processed/        # Datos procesados
├── results/               # Resultados
│   ├── figures/          # Gráficos
│   └── reports/          # Reportes
└── src/                   # Código reutilizable
    └── utils/            # Utilidades
```

## Comandos Útiles

```bash
# Verificar estructura
tree entregas/  # o dir entregas/ en Windows

# Ejecutar scripts
python entregas/entrega_2/setup_dataset.py
python entregas/entrega_2/explore_dask.py

# Ver ayuda de un script
python entregas/entrega_2/explore_dask.py --help
```

## Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'dask'"
```bash
pip install -r requirements.txt
```

### Error: "Directory not found"
Ejecuta primero:
```bash
python entregas/entrega_2/setup_dataset.py
```

### Error al generar gráficos
Asegúrate de tener Graphviz instalado:
```bash
# Windows: descargar de https://graphviz.org/download/
# Linux: sudo apt-get install graphviz
# Mac: brew install graphviz
```

## Recursos

- [Documentación de Dask](https://docs.dask.org/)
- [Tutorial de Dask DataFrames](https://docs.dask.org/en/stable/dataframe.html)
- [Ejemplos de Dask](https://examples.dask.org/)

