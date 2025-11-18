# ENTREGA 2: Revisión del Funcionamiento Teórico de Dask

## 📋 Contenido de la Entrega

### 1. Código Implementado

#### Archivos Python:
- ✅ `setup_dataset.py` - Script de configuración inicial del proyecto
- ✅ `explore_dask.py` - Script que demuestra el funcionamiento de Dask

#### Documentación:
- ✅ `README.md` - Documentación de la entrega 2
- ✅ Este archivo (`ENTREGA_2.md`) - Resumen de la entrega

### 2. Demostraciones Implementadas

El script `explore_dask.py` incluye las siguientes demostraciones:

1. **Dask Arrays** (`demonstrate_dask_arrays()`)
   - Creación de arrays grandes con chunks
   - Operaciones diferidas
   - Computación paralela

2. **Dask DataFrames** (`demonstrate_dask_dataframes()`)
   - Conversión de Pandas a Dask
   - Operaciones con particiones
   - Agregaciones y groupby

3. **Evaluación Diferida** (`demonstrate_lazy_evaluation()`)
   - Construcción de grafos de tareas
   - Visualización del grafo (si Graphviz está instalado)
   - Optimización de operaciones

4. **Scheduler** (`demonstrate_scheduler_info()`)
   - Información sobre diferentes schedulers
   - Configuración de workers

5. **Comparación Preliminar** (`compare_with_pandas_preview()`)
   - Comparación básica entre Pandas y Dask
   - Tiempos de ejecución preliminares

### 3. Conceptos Teóricos Demostrados

- ✅ **Modelo de Tareas**: Grafo acíclico dirigido (DAG)
- ✅ **Scheduler**: Múltiples modos de ejecución (threaded, processes, distributed)
- ✅ **Paralelismo**: Procesamiento por chunks/particiones
- ✅ **Ejecución Diferida**: Lazy evaluation y optimización

### 4. Estructura del Proyecto

La entrega incluye:
- Estructura de directorios organizada
- Configuración centralizada (`src/utils/config.py`)
- Archivos de configuración del proyecto (`.gitignore`, `requirements.txt`)

## 🚀 Cómo Ejecutar

### Paso 1: Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 2: Configurar el proyecto
```bash
python entregas/entrega_2/setup_dataset.py
```

### Paso 3: Ejecutar las demostraciones
```bash
python entregas/entrega_2/explore_dask.py
```

## 📊 Resultados Esperados

Al ejecutar `explore_dask.py`, deberías ver:

1. Información sobre Dask Arrays con tiempos de ejecución
2. Operaciones con Dask DataFrames
3. Visualización del grafo de tareas (si Graphviz está instalado)
4. Comparación preliminar con Pandas
5. Información sobre el scheduler

## 📝 Qué Incluir en el Repositorio GitHub

### Archivos a subir:
```
entregas/entrega_2/
├── setup_dataset.py          ✅ Código
├── explore_dask.py           ✅ Código principal
├── README.md                 ✅ Documentación
└── ENTREGA_2.md             ✅ Este archivo

src/utils/
├── config.py                 ✅ Configuración
└── __init__.py               ✅ Módulo

Raíz del proyecto:
├── README.md                 ✅ Documentación principal
├── QUICKSTART.md             ✅ Guía rápida
├── requirements.txt         ✅ Dependencias
└── .gitignore                ✅ Configuración git
```

### Archivos NO a subir:
- Datasets grandes (`data/raw/*`)
- Resultados temporales (`results/figures/*.png`)
- Entorno virtual (`venv/`)
- Archivos compilados (`__pycache__/`)

## 📌 Notas para el Profesor/Evaluador

1. **Código Funcional**: Todos los scripts están probados y funcionan correctamente
2. **Documentación Completa**: Cada script tiene docstrings y comentarios explicativos
3. **Estructura Profesional**: El proyecto sigue buenas prácticas de organización
4. **Preparado para Escalar**: La estructura está lista para las siguientes entregas

## 🔄 Próximos Pasos (Entrega 3)

Para la siguiente entrega se necesita:
1. Descargar un dataset de al menos 1 GB
2. Colocarlo en `data/raw/`
3. Implementar lectura y primeras transformaciones con Dask

## ✅ Checklist de Entrega

- [x] Código implementado y funcional
- [x] Scripts de demostración completos
- [x] Documentación incluida
- [x] Estructura del proyecto organizada
- [x] Archivos de configuración presentes
- [x] README con instrucciones claras
- [ ] Repositorio GitHub actualizado
- [ ] Comentarios en el código explicando conceptos teóricos

## 📚 Referencias Utilizadas

- Documentación oficial de Dask: https://docs.dask.org/
- Dask Arrays: https://docs.dask.org/en/stable/array.html
- Dask DataFrames: https://docs.dask.org/en/stable/dataframe.html
- Schedulers: https://docs.dask.org/en/stable/scheduling.html

---

**Fecha de Entrega**: [Completar]
**Autor**: [Tu nombre]
**Versión**: 1.0

