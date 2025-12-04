"""
Script para verificar e instalar dependencias del proyecto
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
        'seaborn': 'Seaborn',
        'psutil': 'psutil',
        'tqdm': 'tqdm'
    }
    
    missing_packages = []
    installed_packages = []
    
    print("\n" + "="*70)
    print("VERIFICACIÓN DE DEPENDENCIAS")
    print("="*70 + "\n")
    
    for package, name in required_packages.items():
        try:
            __import__(package)
            print(f"✓ {name:15} - Instalado")
            installed_packages.append(name)
        except ImportError:
            print(f"✗ {name:15} - NO instalado")
            missing_packages.append(package)
    
    print("\n" + "="*70)
    
    if missing_packages:
        print(f"\n⚠ FALTAN {len(missing_packages)} PAQUETE(S):")
        for pkg in missing_packages:
            print(f"   - {pkg}")
        print(f"\n✓ INSTALADOS: {len(installed_packages)}/{len(required_packages)}")
        return False
    else:
        print(f"\n✓ TODAS LAS DEPENDENCIAS ESTÁN INSTALADAS")
        print(f"  ({len(installed_packages)}/{len(required_packages)} paquetes)")
        return True

def install_dependencies():
    """Instala las dependencias desde requirements.txt"""
    project_root = Path(__file__).parent
    requirements_file = project_root / "requirements.txt"
    
    if not requirements_file.exists():
        print(f"\n✗ No se encontró: {requirements_file}")
        return False
    
    print("\n" + "="*70)
    print("INSTALANDO DEPENDENCIAS")
    print("="*70)
    print(f"\nArchivo: {requirements_file}")
    print("\nEjecutando: pip install -r requirements.txt")
    print("="*70 + "\n")
    
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", str(requirements_file)],
            check=True
        )
        print("\n" + "="*70)
        print("✓ DEPENDENCIAS INSTALADAS EXITOSAMENTE")
        print("="*70 + "\n")
        return True
    except subprocess.CalledProcessError as e:
        print("\n" + "="*70)
        print("✗ ERROR AL INSTALAR DEPENDENCIAS")
        print("="*70)
        print(f"\nCódigo de error: {e.returncode}")
        print("\nPor favor, instala manualmente:")
        print(f"  pip install -r {requirements_file}")
        print("\nO instala los paquetes individualmente:")
        print("  pip install dask pandas numpy matplotlib seaborn psutil tqdm")
        print("="*70 + "\n")
        return False

def main():
    """Función principal"""
    print("\n" + "="*70)
    print("VERIFICADOR DE DEPENDENCIAS - PROYECTO DASK")
    print("="*70)
    
    # Verificar dependencias
    if check_dependencies():
        print("\n✅ Todo listo. Puedes ejecutar el proyecto.")
        return
    
    # Si faltan dependencias, ofrecer instalarlas
    print("\n⚠ FALTAN DEPENDENCIAS")
    respuesta = input("\n¿Deseas instalar las dependencias ahora? (s/n): ").lower()
    
    if respuesta == 's':
        if install_dependencies():
            # Verificar nuevamente
            print("\nVerificando nuevamente...")
            if check_dependencies():
                print("\n✅ Todas las dependencias instaladas correctamente.")
            else:
                print("\n⚠ Aún faltan algunas dependencias.")
                print("   Intenta instalar manualmente: pip install -r requirements.txt")
        else:
            print("\n❌ No se pudieron instalar las dependencias automáticamente.")
            print("   Por favor, instálalas manualmente.")
    else:
        print("\n📝 Para instalar manualmente, ejecuta:")
        print("   pip install -r requirements.txt")

if __name__ == "__main__":
    main()

