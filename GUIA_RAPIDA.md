# 🚀 Guía Rápida - Proyecto Dask

## ⚡ Inicio Rápido (5 minutos)

### 1. Instalar
```bash
pip install -r requirements.txt
```

### 2. Generar datos de prueba (si no tienes dataset)
```bash
python entregas/entrega_3/generate_sample_data.py
```

### 3. Ejecutar todo
```bash
python run_complete_pipeline.py
```

**¡Listo!** Los resultados estarán en `results/`

---

## 📋 Qué Hace Cada Script

| Script | Qué Hace | Tiempo |
|--------|----------|--------|
| `setup_dataset.py` | Configura el proyecto | 10s |
| `explore_dask.py` | Muestra ejemplos de Dask | 30s |
| `read_data_dask.py` | Lee archivo y compara | 1-5 min |
| `transform_data_dask.py` | Limpia y transforma | 2-10 min |
| `compare_pandas_dask.py` | Compara rendimiento | 5-15 min |
| `visualize_results.py` | Genera gráficos | 10s |

---

## 🎯 Resultados que Obtienes

```
results/
├── figures/
│   ├── time_comparison.png      ← Gráfico de tiempos
│   ├── memory_comparison.png    ← Gráfico de memoria
│   ├── speedup_analysis.png     ← Análisis de velocidad
│   └── comparison_table.png     ← Tabla comparativa
│
└── reports/
    └── summary_report.txt       ← Reporte completo
```

---

## 💡 Tips

1. **Primera vez**: Usa datos sintéticos para probar
2. **Dataset real**: Descarga uno de Kaggle (1-5 GB)
3. **Problemas**: Revisa los mensajes de error, son descriptivos
4. **Personalizar**: Edita los scripts según tu dataset

---

## ❓ Preguntas Frecuentes

**P: ¿Necesito un dataset real?**  
R: No, puedes usar el generador de datos sintéticos.

**P: ¿Cuánto tiempo tarda todo?**  
R: Depende del tamaño del dataset. Con 2GB: ~20-30 minutos.

**P: ¿Puedo saltarme alguna entrega?**  
R: Sí, pero es mejor seguir el orden.

**P: ¿Funciona en Windows?**  
R: Sí, funciona en Windows, Linux y Mac.

---

**¿Listo para empezar?** → `python run_complete_pipeline.py` 🚀

