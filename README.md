# 🚀 Proyecto Dask: Análisis Paralelo y Escalable de Datos Masivos

## 📋 Descripción del Proyecto

Este proyecto **evalúa y compara** el rendimiento de **Dask** vs **Pandas** para el análisis de datos masivos. Demuestra cuándo usar cada herramienta y por qué, con ejemplos prácticos y resultados medibles.

### 🎯 Objetivo

Demostrar que **Dask es mejor para archivos grandes** (>1GB) que no caben en memoria, mientras que **Pandas es más rápido para archivos pequeños** (<500MB).

---

## 🤔 ¿Qué es este proyecto?

### El Problema

Imagina que tienes un archivo Excel **gigante**:

```
📊 Tu archivo: 5 GB de datos
💻 Tu computadora: 8 GB de RAM
❌ Pandas intenta cargar TODO → ¡CRASH! 💥
```

**Pandas**:
- ✅ Funciona bien con archivos pequeños (< 500 MB)
- ❌ Falla con archivos grandes (> 1 GB)
- ❌ No usa todos los núcleos del procesador
- ❌ Lento cuando hay muchos datos

### La Solución: Dask

**Dask**:
- ✅ Divide el archivo en pedazos pequeños (chunks)
- ✅ Procesa cada pedazo por separado
- ✅ Usa todos los núcleos del procesador (paralelismo)
- ✅ Puede manejar archivos de cualquier tamaño

**Analogía Simple**:
- **Pandas** = Intentar cargar un camión completo de una vez → Se rompe
- **Dask** = Cargar el camión en varios viajes pequeños → Funciona perfecto

---

## 📦 ¿Qué hace cada entrega?

### 📍 Entrega 2: "Aprender sobre Dask"

**¿Qué hace?**
- Te enseña cómo funciona Dask
- Muestra ejemplos básicos
- Compara conceptos teóricos

**Archivos**:
- `setup_dataset.py` - Configura el proyecto
- `explore_dask.py` - Ejemplos prácticos

**Ejecutar**:
```bash
python entregas/entrega_2/setup_dataset.py
python entregas/entrega_2/explore_dask.py
```

**Resultado**: Entiendes qué es Dask y cómo funciona.

---

### 📍 Entrega 3: "Usar Dask con datos reales"

**¿Qué hace?**
1. **Lee un archivo grande** (que Pandas no puede)
2. **Limpia los datos** (elimina duplicados, valores nulos)
3. **Transforma los datos** (cambia formatos, crea nuevas columnas)
4. **Agrupa y resume** (calcula promedios, sumas, etc.)

**Archivos**:
- `read_data_dask.py` - Lee el archivo y compara con Pandas
- `transform_data_dask.py` - Limpia y transforma los datos
- `generate_sample_data.py` - Genera datos de prueba (si no tienes dataset)

**Ejecutar**:
```bash
# Si no tienes dataset, genera uno:
python entregas/entrega_3/generate_sample_data.py

# Luego procesa:
python entregas/entrega_3/read_data_dask.py
python entregas/entrega_3/transform_data_dask.py
```

**Resultado**: Tienes datos limpios y procesados listos para analizar.

---

### 📍 Entrega 4: "Comparar Pandas vs Dask"

**¿Qué hace?**
- Ejecuta las **mismas operaciones** con ambas herramientas
- Mide el **tiempo** que tarda cada una
- Mide la **memoria** que usa cada una
- Calcula cuál es **más rápida**

**Archivo**:
- `compare_pandas_dask.py` - Hace las comparaciones

**Ejecutar**:
```bash
python entregas/entrega_4/compare_pandas_dask.py
```

**Resultado**: Sabes exactamente cuándo usar cada herramienta.

---

### 📍 Entrega 5: "Mostrar los resultados"

**¿Qué hace?**
- Crea **gráficos bonitos** comparando Pandas y Dask
- Genera un **reporte** con las conclusiones
- Muestra **tablas** con todos los números

**Archivo**:
- `visualize_results.py` - Genera gráficos y reportes

**Ejecutar**:
```bash
python entregas/entrega_5/visualize_results.py
```

**Resultado**: Tienes visualizaciones profesionales de los resultados.

---

## 🚀 Cómo Usar el Proyecto

### Opción 1: Todo Automático (Recomendado) ⭐

```bash
# 1. Instalar dependencias
python check_dependencies.py

# 2. Generar datos de prueba (si no tienes dataset)
python entregas/entrega_3/generate_sample_data.py

# 3. Ejecutar todo
python run_complete_pipeline.py
```

**¡Listo!** Los resultados estarán en `results/`

---

### Opción 2: Paso a Paso

```bash
# 1. Verificar e instalar dependencias
python check_dependencies.py

# 2. Configurar (solo la primera vez)
python entregas/entrega_2/setup_dataset.py

# 3. Explorar Dask
python entregas/entrega_2/explore_dask.py

# 4. Generar datos (si no tienes dataset)
python entregas/entrega_3/generate_sample_data.py

# 5. Leer datos
python entregas/entrega_3/read_data_dask.py

# 6. Transformar datos
python entregas/entrega_3/transform_data_dask.py

# 7. Comparar
python entregas/entrega_4/compare_pandas_dask.py

# 8. Visualizar
python entregas/entrega_5/visualize_results.py
```

---

## 📊 Resultados que Obtienes

### Gráficos Generados (en `results/figures/`):

1. **time_comparison.png** 
   - Muestra cuánto tiempo tarda cada herramienta
   - ¿Cuál es más rápida?

2. **memory_comparison.png**
   - Muestra cuánta memoria usa cada herramienta
   - ¿Cuál es más eficiente?

3. **speedup_analysis.png**
   - Muestra cuántas veces más rápido es Dask
   - Análisis de velocidad

4. **comparison_table.png**
   - Tabla con todos los números
   - Comparación completa

### Reportes Generados (en `results/reports/`):

- **summary_report.txt**
  - Conclusiones principales
  - Métricas detalladas
  - Recomendaciones

### Datos Procesados (en `data/processed/`):

- **processed_data.parquet** - Datos limpios y transformados
- **benchmark_results.csv** - Métricas de rendimiento

---

## 🎓 Conceptos Clave Explicados Simple

### 1. Chunks (Bloques)

**¿Qué es?**
Dask divide el archivo grande en pedazos pequeños.

**Ejemplo**:
```
Archivo grande (5 GB)
    ↓
Dask lo divide en:
  - Chunk 1 (100 MB)
  - Chunk 2 (100 MB)
  - Chunk 3 (100 MB)
  - ... (50 chunks en total)
```

**Ventaja**: Solo carga en memoria lo que necesita, no todo.

---

### 2. Paralelismo

**¿Qué es?**
Procesar varias cosas al mismo tiempo.

**Pandas**:
```
[Tarea 1] → [Tarea 2] → [Tarea 3]
Una a la vez (secuencial)
```

**Dask**:
```
[Tarea 1] ┐
[Tarea 2] ├→ Todas al mismo tiempo (paralelo)
[Tarea 3] ┘
```

**Ventaja**: Más rápido porque usa todos los núcleos del CPU.

---

### 3. Lazy Evaluation (Evaluación Diferida)

**¿Qué es?**
Dask planifica primero, ejecuta después.

**Pandas**:
```
Leer → Procesar → Mostrar
(Hace todo inmediatamente)
```

**Dask**:
```
Planear → (esperar) → Ejecutar cuando sea necesario
(Puede optimizar antes de ejecutar)
```

**Ventaja**: Puede optimizar antes de ejecutar.

---

## 📈 Resultados Esperados

### Con un Dataset de 2 GB:

| Operación | Pandas | Dask | Ventaja |
|-----------|--------|------|---------|
| Lectura | ❌ Falla | ✅ 30s | Dask funciona |
| Filtrado | ❌ Falla | ✅ 45s | Dask funciona |
| Agrupación | ❌ Falla | ✅ 60s | Dask funciona |

**Conclusión**: Con archivos grandes, **solo Dask funciona**.

---

### Con un Dataset de 500 MB:

| Operación | Pandas | Dask | Ventaja |
|-----------|--------|------|---------|
| Lectura | ✅ 5s | ✅ 8s | Pandas más rápido |
| Filtrado | ✅ 3s | ✅ 4s | Pandas más rápido |
| Agrupación | ✅ 10s | ✅ 12s | Pandas más rápido |

**Conclusión**: Con archivos pequeños, **Pandas es más rápido** (menos overhead).

---

### Regla General:

| Tamaño del Archivo | Usa |
|-------------------|-----|
| < 500 MB | **Pandas** (más rápido) |
| 500 MB - 1 GB | **Cualquiera** (similar) |
| > 1 GB | **Dask** (única opción) |

---

## 🛠️ Instalación

### 1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd Dask
```

### 2. Crear un entorno virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias:

**Opción A - Automática (Recomendada):**
```bash
python check_dependencies.py
```
Este script verificará e instalará automáticamente las dependencias faltantes.

**Opción B - Manual:**
```bash
pip install -r requirements.txt
```

**Si tienes problemas, instala las dependencias principales:**
```bash
pip install dask pandas numpy matplotlib seaborn psutil tqdm pyarrow fastparquet
```

---

## 📁 Estructura del Proyecto

```
Dask/
├── entregas/                    # Código organizado por entregas
│   ├── entrega_2/              # ✅ Fundamentos teóricos de Dask
│   │   ├── setup_dataset.py    # Configuración inicial
│   │   ├── explore_dask.py     # Demostraciones de Dask
│   │   └── README.md           # Documentación específica
│   ├── entrega_3/              # ✅ Procesamiento de datos
│   │   ├── read_data_dask.py   # Lectura de datasets
│   │   ├── transform_data_dask.py  # Transformaciones
│   │   ├── generate_sample_data.py  # Generador de datos sintéticos
│   │   └── README.md
│   ├── entrega_4/              # ✅ Comparación de rendimiento
│   │   ├── compare_pandas_dask.py   # Benchmark completo
│   │   └── README.md
│   └── entrega_5/              # ✅ Visualización
│       ├── visualize_results.py    # Gráficos y reportes
│       └── README.md
│
├── data/                       # Datasets (no incluidos en git)
│   ├── raw/                   # Datos originales (CSV)
│   └── processed/              # Datos procesados (Parquet)
│
├── results/                    # Resultados generados
│   ├── figures/               # Gráficos (PNG)
│   │   ├── time_comparison.png
│   │   ├── memory_comparison.png
│   │   ├── speedup_analysis.png
│   │   └── comparison_table.png
│   └── reports/               # Reportes (TXT)
│       └── summary_report.txt
│
├── src/                        # Código reutilizable
│   ├── utils/                 # Utilidades
│   │   └── config.py          # Configuración centralizada
│   └── benchmarks/            # Herramientas de benchmarking
│       └── benchmark_utils.py
│
├── check_dependencies.py       # Verificador de dependencias
├── run_complete_pipeline.py    # Script maestro (ejecuta todo)
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Este archivo
```

---

## ✅ Requisitos

### Software
- **Python 3.8+** (recomendado 3.9 o superior)
- Todas las dependencias en `requirements.txt`

### Hardware Recomendado
- **RAM**: Mínimo 8 GB (recomendado 16 GB)
- **Disco**: 5-10 GB libres para datasets y resultados
- **CPU**: Múltiples núcleos (Dask aprovecha paralelismo)

### Datos
- **Opción 1**: Dataset CSV de 1-5 GB en `data/raw/`
- **Opción 2**: Usar generador de datos sintéticos (incluido)

### Dependencias Principales
- `dask` - Procesamiento paralelo y distribuido
- `pandas` - Análisis de datos (comparación)
- `numpy` - Operaciones numéricas
- `matplotlib` / `seaborn` - Visualizaciones
- `psutil` - Medición de memoria
- `pyarrow` / `fastparquet` - Formato Parquet

---

## 🆘 Solución de Problemas

### ❌ Error: "ModuleNotFoundError: No module named 'dask'"
**Solución:**
```bash
python check_dependencies.py
# O manualmente:
pip install -r requirements.txt
```

### ❌ Error: "No se encontraron archivos de datos"
**Solución:**
```bash
# Generar datos sintéticos
python entregas/entrega_3/generate_sample_data.py

# O colocar un CSV en data/raw/
```

### ❌ Error: "Directory not found"
**Solución:**
```bash
python entregas/entrega_2/setup_dataset.py
```

### ❌ Pandas falla con archivo grande
**Es normal**: Pandas no puede con archivos muy grandes. Eso es exactamente lo que demuestra el proyecto.

### ❌ Error al guardar en Parquet
**Solución**: El script intentará automáticamente con diferentes engines. Si falla, guardará como CSV.

---

## 📋 Plan de Trabajo

- ✅ **Semana 1**: Selección del dataset y diseño del experimento
- ✅ **Semana 2**: Revisión del funcionamiento teórico de Dask (COMPLETA)
- ✅ **Semana 3**: Lectura y primeras transformaciones con Dask (COMPLETA)
- ✅ **Semana 4**: Implementación de las mismas tareas con Pandas para comparación (COMPLETA)
- ✅ **Semana 5**: Medición, análisis y visualización de resultados (COMPLETA)
- ⏳ **Semana 6**: Redacción del informe técnico en formato IEEE
- ⏳ **Semana 7**: Ajustes finales, documentación y preparación del repositorio

---

## 🎯 Estado del Proyecto

✅ **Código Completo**: Entregas 2-5 implementadas y listas para usar
✅ **Documentación**: Completa y actualizada
✅ **Scripts Funcionales**: Todos probados y documentados
✅ **Generador de Datos**: Incluido para pruebas sin dataset real
✅ **Visualizaciones**: Gráficos y reportes automáticos
⏳ **Pendiente**: Dataset real (opcional) e informe final IEEE

---

## 🎓 Resumen en 3 Puntos

1. **Dask es mejor para archivos grandes** que no caben en memoria
2. **Pandas es más rápido para archivos pequeños** (menos overhead)
3. **Este proyecto demuestra cuándo usar cada uno** con datos reales

---

## 📚 Recursos Adicionales

- [Documentación de Dask](https://docs.dask.org/)
- [Tutorial de Dask DataFrames](https://docs.dask.org/en/stable/dataframe.html)
- [Ejemplos de Dask](https://examples.dask.org/)

---

## 👤 Autor

**Mauro Espinoza**

---

## 📄 Licencia

Este proyecto es parte de un trabajo académico.

---

## 🚀 ¡Listo para Empezar!

```bash
# 1. Instalar dependencias
python check_dependencies.py

# 2. Generar datos (opcional)
python entregas/entrega_3/generate_sample_data.py

# 3. Ejecutar todo
python run_complete_pipeline.py
```

**¡Éxito con tu proyecto!** 🎉
