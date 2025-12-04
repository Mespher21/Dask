# 📦 ENTREGA FINAL - Proyecto Dask

## 🎯 Información del Proyecto

**Título**: Uso de Dask para el Análisis Paralelo y Escalable de Datos Masivos en Python

**Autor**: Mauro Espinoza

**Repositorio GitHub**: [https://github.com/Mespher21/Dask](https://github.com/Mespher21/Dask)

---

## 📋 Descripción

Este proyecto evalúa el rendimiento y la escalabilidad de **Dask** en el análisis de datos masivos, comparándolo con **Pandas** para identificar sus ventajas, desventajas y posibles aplicaciones prácticas.

### Objetivo Principal

Demostrar cuándo y por qué usar Dask en lugar de Pandas para el análisis de datos grandes, mediante experimentos prácticos y comparaciones de rendimiento.

---

## 🗂️ Estructura del Proyecto

El proyecto está organizado en **5 entregas** que cubren desde los fundamentos teóricos hasta la visualización de resultados:

### 📍 Entrega 2: Fundamentos Teóricos de Dask
**Ubicación**: `entregas/entrega_2/`

**Contenido**:
- `setup_dataset.py` - Configuración inicial del proyecto
- `explore_dask.py` - Demostraciones de conceptos básicos de Dask
- `README.md` - Documentación específica

**Objetivo**: Entender cómo funciona Dask (Arrays, DataFrames, lazy evaluation, paralelismo)

---

### 📍 Entrega 3: Procesamiento de Datos con Dask
**Ubicación**: `entregas/entrega_3/`

**Contenido**:
- `read_data_dask.py` - Lectura de datasets grandes y comparación con Pandas
- `transform_data_dask.py` - Limpieza, transformación y procesamiento de datos
- `generate_sample_data.py` - Generador de datos sintéticos para pruebas
- `README.md` - Documentación específica

**Objetivo**: Implementar un pipeline completo de procesamiento de datos usando Dask

---

### 📍 Entrega 4: Comparación de Rendimiento
**Ubicación**: `entregas/entrega_4/`

**Contenido**:
- `compare_pandas_dask.py` - Benchmark completo comparando Pandas vs Dask
- `README.md` - Documentación específica

**Objetivo**: Medir y comparar tiempos de ejecución, uso de memoria y eficiencia

---

### 📍 Entrega 5: Visualización de Resultados
**Ubicación**: `entregas/entrega_5/`

**Contenido**:
- `visualize_results.py` - Generación de gráficos y reportes comparativos
- `README.md` - Documentación específica

**Objetivo**: Visualizar y documentar los resultados del experimento

---

## 📊 Resultados Generados

### Gráficos (`results/figures/`)
- `time_comparison.png` - Comparación de tiempos de ejecución
- `memory_comparison.png` - Comparación de uso de memoria
- `speedup_analysis.png` - Análisis de velocidad (speedup)
- `comparison_table.png` - Tabla comparativa completa

### Reportes (`results/reports/`)
- `summary_report.txt` - Resumen ejecutivo con conclusiones y métricas

---

## 🛠️ Componentes Adicionales

### Scripts Principales
- `run_complete_pipeline.py` - Script maestro que ejecuta todas las entregas en secuencia
- `check_dependencies.py` - Verificador e instalador automático de dependencias

### Código Reutilizable (`src/`)
- `src/utils/config.py` - Configuración centralizada del proyecto
- `src/benchmarks/benchmark_utils.py` - Utilidades para medición de rendimiento

### Documentación
- `README.md` - Documentación completa del proyecto (instalación, uso, explicaciones)
- `requirements.txt` - Lista de dependencias del proyecto

---

## 🚀 Cómo Usar el Proyecto

### Instalación Rápida

```bash
# 1. Clonar el repositorio
git clone https://github.com/Mespher21/Dask.git
cd Dask

# 2. Instalar dependencias
python check_dependencies.py

# 3. Generar datos sintéticos (opcional)
python entregas/entrega_3/generate_sample_data.py

# 4. Ejecutar pipeline completo
python run_complete_pipeline.py
```

### Ejecución por Entregas

Ver el `README.md` principal en el repositorio para instrucciones detalladas de cada entrega.

---

## 📈 Resultados Principales

El proyecto demuestra que:

1. **Dask es esencial** para datasets mayores que la RAM disponible
2. **Pandas es más rápido** para archivos pequeños (<500MB) debido a menos overhead
3. **Dask aprovecha el paralelismo** mejorando tiempos en operaciones CPU-intensivas
4. **La API de Dask es similar a Pandas**, facilitando la migración

### Regla General

| Tamaño del Archivo | Herramienta Recomendada |
|-------------------|------------------------|
| < 500 MB | Pandas (más rápido) |
| 500 MB - 1 GB | Cualquiera (similar) |
| > 1 GB | Dask (única opción viable) |

---

## ✅ Estado del Proyecto

- ✅ **Código Completo**: Todas las entregas (2-5) implementadas y funcionales
- ✅ **Documentación**: README completo con explicaciones detalladas
- ✅ **Resultados**: Gráficos y reportes generados
- ✅ **Scripts Funcionales**: Pipeline completo automatizado
- ✅ **Generador de Datos**: Incluido para pruebas sin dataset real

---

## 📚 Tecnologías Utilizadas

- **Python 3.8+**
- **Dask** - Procesamiento paralelo y distribuido
- **Pandas** - Análisis de datos (para comparación)
- **NumPy** - Operaciones numéricas
- **Matplotlib/Seaborn** - Visualizaciones
- **PyArrow/FastParquet** - Formato Parquet para almacenamiento eficiente

---

## 🔗 Enlaces

- **Repositorio GitHub**: [https://github.com/Mespher21/Dask](https://github.com/Mespher21/Dask)
- **Documentación Dask**: https://docs.dask.org/
- **Documentación Pandas**: https://pandas.pydata.org/

---

## 📝 Notas Finales

Todo el código, documentación, resultados y scripts se encuentran disponibles en el repositorio de GitHub mencionado arriba. El proyecto está completamente funcional y listo para ser ejecutado siguiendo las instrucciones del `README.md` principal.

Para cualquier duda o consulta sobre el proyecto, revisar la documentación en el repositorio o contactar al autor.

---

**Autor**: Mauro Espinoza  
**Fecha**: 2025  
**Curso**: Computación Paralela y Distribuida

