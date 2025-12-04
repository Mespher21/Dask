"""
Script maestro para ejecutar el pipeline completo del proyecto
Ejecuta todas las entregas en secuencia
"""

import subprocess
import sys
from pathlib import Path

def check_dependencies():
    """Verifica que las dependencias principales estén instaladas"""
    required_packages = {
        'dask': 'Dask',
        'pandas': 'Pandas',
        'numpy': 'NumPy',
        'matplotlib': 'Matplotlib',
        'seaborn': 'Seaborn'
    }
    
    missing_packages = []
    
    print("\n" + "="*70)
    print("VERIFICANDO DEPENDENCIAS")
    print("="*70)
    
    for package, name in required_packages.items():
        try:
            __import__(package)
            print(f"✓ {name} instalado")
        except ImportError:
            print(f"✗ {name} NO instalado")
            missing_packages.append(name)
    
    if missing_packages:
        print(f"\n⚠ FALTAN LOS SIGUIENTES PAQUETES: {', '.join(missing_packages)}")
        print("\nOpciones:")
        print("1. Instalar automáticamente: pip install -r requirements.txt")
        print("2. Instalar manualmente: pip install " + " ".join(missing_packages))
        print("\n" + "="*70)
        return False
    
    print("\n✓ Todas las dependencias están instaladas")
    print("="*70 + "\n")
    return True

def install_dependencies():
    """Intenta instalar las dependencias faltantes"""
    print("\n" + "="*70)
    print("INSTALANDO DEPENDENCIAS")
    print("="*70)
    
    requirements_file = Path(__file__).parent / "requirements.txt"
    
    if not requirements_file.exists():
        print("✗ No se encontró requirements.txt")
        return False
    
    try:
        print(f"\nEjecutando: pip install -r {requirements_file}")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", str(requirements_file)],
            check=True
        )
        print("\n✓ Dependencias instaladas exitosamente")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Error al instalar dependencias")
        print(f"  Código de error: {e.returncode}")
        print("\nPor favor, instala manualmente:")
        print(f"  pip install -r {requirements_file}")
        return False

def run_script(script_path, description):
    """Ejecuta un script de Python y muestra el resultado"""
    print("\n" + "="*70)
    print(f"EJECUTANDO: {description}")
    print("="*70)
    
    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            check=True,
            capture_output=False
        )
        print(f"\n✓ {description} completado exitosamente")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Error al ejecutar {description}")
        print(f"  Código de error: {e.returncode}")
        return False
    except FileNotFoundError:
        print(f"\n✗ Script no encontrado: {script_path}")
        return False

def main():
    """Función principal"""
    project_root = Path(__file__).parent
    
    print("\n" + "="*70)
    print("PIPELINE COMPLETO DEL PROYECTO DASK")
    print("="*70)
    print("\nEste script ejecutará todas las entregas en secuencia:")
    print("  1. Entrega 2: Configuración y exploración de Dask")
    print("  2. Entrega 3: Lectura y transformaciones con Dask")
    print("  3. Entrega 4: Comparación con Pandas")
    print("  4. Entrega 5: Visualización de resultados")
    print("\n" + "="*70)
    
    # Verificar dependencias PRIMERO
    if not check_dependencies():
        print("\n⚠ DEPENDENCIAS FALTANTES DETECTADAS")
        respuesta = input("\n¿Deseas instalar las dependencias ahora? (s/n): ").lower()
        if respuesta == 's':
            if not install_dependencies():
                print("\n❌ No se pudieron instalar las dependencias.")
                print("Por favor, instálalas manualmente antes de continuar:")
                print("  pip install -r requirements.txt")
                return
            # Verificar nuevamente después de instalar
            if not check_dependencies():
                print("\n❌ Aún faltan dependencias después de la instalación.")
                print("Por favor, verifica manualmente.")
                return
        else:
            print("\n❌ No se pueden ejecutar los scripts sin las dependencias.")
            print("Instala las dependencias con: pip install -r requirements.txt")
            return
    
    respuesta = input("\n¿Deseas continuar con la ejecución? (s/n): ").lower()
    if respuesta != 's':
        print("Operación cancelada.")
        return
    
    # Pipeline de ejecución
    scripts = [
        (project_root / "entregas" / "entrega_2" / "setup_dataset.py",
         "Entrega 2: Configuración inicial"),
        
        (project_root / "entregas" / "entrega_2" / "explore_dask.py",
         "Entrega 2: Exploración de Dask"),
        
        (project_root / "entregas" / "entrega_3" / "read_data_dask.py",
         "Entrega 3: Lectura de datos con Dask"),
        
        (project_root / "entregas" / "entrega_3" / "transform_data_dask.py",
         "Entrega 3: Transformaciones de datos"),
        
        (project_root / "entregas" / "entrega_4" / "compare_pandas_dask.py",
         "Entrega 4: Comparación Pandas vs Dask"),
        
        (project_root / "entregas" / "entrega_5" / "visualize_results.py",
         "Entrega 5: Visualización de resultados"),
    ]
    
    # Verificar si hay dataset, si no, sugerir generarlo
    data_dir = project_root / "data" / "raw"
    csv_files = list(data_dir.glob("*.csv")) if data_dir.exists() else []
    
    if len(csv_files) == 0:
        print("\n⚠ No se encontró ningún dataset CSV en data/raw/")
        print("\nOpciones:")
        print("1. Generar datos sintéticos:")
        print("   python entregas/entrega_3/generate_sample_data.py")
        print("2. Descargar un dataset real y colocarlo en data/raw/")
        print("\n¿Deseas generar datos sintéticos ahora? (s/n): ", end="")
        respuesta = input().lower()
        if respuesta == 's':
            gen_script = project_root / "entregas" / "entrega_3" / "generate_sample_data.py"
            if gen_script.exists():
                run_script(gen_script, "Generación de datos sintéticos")
            else:
                print("⚠ Script de generación no encontrado")
        print()
    
    resultados = []
    
    for script_path, description in scripts:
        if script_path.exists():
            exito = run_script(script_path, description)
            resultados.append((description, exito))
            
            if not exito:
                print(f"\n⚠ Error en {description}")
                # Verificar si es un error de dependencias
                if "ModuleNotFoundError" in str(exito) or "No module named" in str(exito):
                    print("\n💡 Este error probablemente se debe a dependencias faltantes.")
                    print("   Ejecuta: pip install -r requirements.txt")
                continuar = input("\n¿Deseas continuar con el siguiente paso? (s/n): ").lower()
                if continuar != 's':
                    break
        else:
            print(f"\n⚠ Script no encontrado: {script_path}")
            resultados.append((description, False))
    
    # Resumen final
    print("\n" + "="*70)
    print("RESUMEN DE EJECUCIÓN")
    print("="*70)
    
    for desc, exito in resultados:
        estado = "✓" if exito else "✗"
        print(f"{estado} {desc}")
    
    exitosos = sum(1 for _, exito in resultados if exito)
    total = len(resultados)
    
    print(f"\nCompletados: {exitosos}/{total}")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()

