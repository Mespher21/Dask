"""
Script de configuración inicial para la Entrega 2
Selección y preparación del dataset para el experimento
"""

import os
import sys
from pathlib import Path

# Agregar el directorio raíz al path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

def create_directory_structure():
    """Crea la estructura de directorios necesaria para el proyecto"""
    directories = [
        project_root / "data" / "raw",
        project_root / "data" / "processed",
        project_root / "results" / "figures",
        project_root / "results" / "reports",
        project_root / "src" / "utils",
        project_root / "src" / "benchmarks",
        project_root / "docs"
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        # Crear archivo .gitkeep para mantener la estructura en git
        (directory / ".gitkeep").touch(exist_ok=True)
        print(f"✓ Directorio creado: {directory}")
    
    print("\n✓ Estructura de directorios creada exitosamente\n")

def check_dependencies():
    """Verifica que las dependencias principales estén instaladas"""
    required_packages = {
        'dask': 'Dask',
        'pandas': 'Pandas',
        'numpy': 'NumPy'
    }
    
    missing_packages = []
    
    for package, name in required_packages.items():
        try:
            __import__(package)
            print(f"✓ {name} instalado")
        except ImportError:
            print(f"✗ {name} NO instalado")
            missing_packages.append(name)
    
    if missing_packages:
        print(f"\n⚠ Advertencia: Faltan los siguientes paquetes: {', '.join(missing_packages)}")
        print("  Ejecuta: pip install -r requirements.txt\n")
        return False
    
    print("\n✓ Todas las dependencias están instaladas\n")
    return True

def get_dataset_info():
    """Muestra información sobre los datasets recomendados"""
    print("=" * 70)
    print("DATASETS RECOMENDADOS PARA EL EXPERIMENTO")
    print("=" * 70)
    print("\n1. Kaggle Datasets:")
    print("   - NYC Taxi Trip Data (varios GB)")
    print("   - Amazon Product Reviews")
    print("   - Google Play Store Apps")
    print("\n2. ERA5 Climate Data:")
    print("   - Datos climáticos reanálisis (1-5 GB)")
    print("   - Disponible en: https://cds.climate.copernicus.eu/")
    print("\n3. Datasets de ejemplo para pruebas:")
    print("   - Puedes generar datos sintéticos para pruebas iniciales")
    print("\n" + "=" * 70 + "\n")

def main():
    """Función principal"""
    print("=" * 70)
    print("CONFIGURACIÓN INICIAL - ENTREGA 2")
    print("Proyecto: Uso de Dask para Análisis de Datos Masivos")
    print("=" * 70 + "\n")
    
    # Crear estructura de directorios
    print("1. Creando estructura de directorios...")
    create_directory_structure()
    
    # Verificar dependencias
    print("2. Verificando dependencias...")
    deps_ok = check_dependencies()
    
    # Información sobre datasets
    print("3. Información sobre datasets...")
    get_dataset_info()
    
    print("=" * 70)
    print("CONFIGURACIÓN COMPLETADA")
    print("=" * 70)
    print("\nPróximos pasos:")
    print("1. Descargar un dataset de al menos 1 GB")
    print("2. Colocarlo en: data/raw/")
    print("3. Ejecutar: python entregas/entrega_2/explore_dask.py")
    print("\n")

if __name__ == "__main__":
    main()

