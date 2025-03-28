#!/usr/bin/env python3
import os
import subprocess
import shutil
import platform
from pathlib import Path

# Ruta donde se clonará y construirá fastfetch
FASTFETCH_DIR = Path.home() / "apps" / "fastfetch"
# Ruta al binario de fastfetch después de compilarlo
FASTFETCH_BIN = FASTFETCH_DIR / "build" / "fastfetch"

# Lista de dependencias necesarias para compilar fastfetch
DEPENDENCIAS = ["git", "cmake", "make", "gcc"]

def comando_disponible(comando):
    """
    Verifica si un comando está disponible en el sistema.
    Utiliza shutil.which para buscar el comando en el PATH.
    """
    return shutil.which(comando) is not None

def instalar_dependencias():
    """
    Verifica si las dependencias necesarias están instaladas.
    Si faltan dependencias, las instala según la distribución detectada.
    """
    print("[+] Verificando dependencias...")

    # Lista de dependencias faltantes
    faltantes = [cmd for cmd in DEPENDENCIAS if not comando_disponible(cmd)]
    if not faltantes:
        print("[✓] Todas las dependencias están presentes.")
        return

    print(f"[!] Faltan dependencias: {', '.join(faltantes)}")
    # Detecta la distribución del sistema operativo
    distro = detectar_distro()

    # Instala las dependencias según la distribución
    if distro == "debian":
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "install", "-y"] + faltantes)
    elif distro == "arch":
        subprocess.run(["sudo", "pacman", "-Sy", "--noconfirm"] + faltantes)
    elif distro == "fedora":
        subprocess.run(["sudo", "dnf", "install", "-y"] + faltantes)
    else:
        # Si la distribución no es soportada, muestra un mensaje y termina el programa
        print("[x] Distro no soportada. Instala manualmente: " + " ".join(faltantes))
        exit(1)

def detectar_distro():
    """
    Detecta la distribución del sistema operativo leyendo el archivo /etc/os-release.
    Retorna el nombre de la distribución: 'debian', 'arch', 'fedora' o 'desconocida'.
    """
    try:
        with open("/etc/os-release") as f:
            contenido = f.read().lower()
            if "debian" in contenido or "ubuntu" in contenido:
                return "debian"
            elif "arch" in contenido:
                return "arch"
            elif "fedora" in contenido:
                return "fedora"
    except:
        pass
    return "desconocida"

def instalar_fastfetch():
    """
    Descarga y compila fastfetch desde su repositorio oficial.
    Si ya está clonado, actualiza el repositorio antes de compilar.
    """
    print("[+] Descargando e instalando fastfetch...")
    if FASTFETCH_DIR.exists():
        # Si el repositorio ya existe, realiza un pull para actualizarlo
        print("[i] fastfetch ya está clonado, actualizando...")
        subprocess.run(["git", "pull"], cwd=FASTFETCH_DIR)
    else:
        # Clona el repositorio en la ruta especificada
        os.makedirs(FASTFETCH_DIR.parent, exist_ok=True)
        subprocess.run(["git", "clone", "https://github.com/fastfetch-cli/fastfetch", str(FASTFETCH_DIR)], check=True)

    # Crea el directorio de compilación y compila fastfetch
    build_dir = FASTFETCH_DIR / "build"
    os.makedirs(build_dir, exist_ok=True)
    subprocess.run(["cmake", ".."], cwd=build_dir, check=True)
    subprocess.run(["make"], cwd=build_dir, check=True)

def ejecutar_fastfetch():
    """
    Ejecuta el binario de fastfetch compilado.
    """
    print("[+] Ejecutando fastfetch...\n")
    subprocess.run([str(FASTFETCH_BIN)])

def main():
    """
    Función principal del script:
    1. Verifica e instala dependencias.
    2. Descarga y compila fastfetch si no está instalado.
    3. Ejecuta fastfetch.
    """
    if FASTFETCH_BIN.exists():
        # Si fastfetch ya está instalado, simplemente lo ejecuta sin mostrar mensajes adicionales
        ejecutar_fastfetch()
    else:
        # Si fastfetch no está instalado, realiza todo el proceso de instalación
        print("[+] Iniciando instalación de fastfetch...")
        instalar_dependencias()
        instalar_fastfetch()
        ejecutar_fastfetch()

        # Mensaje final
        print("\n[✓] El programa ha terminado. Fastfetch ha sido instalado y ejecutado correctamente.")
        print("[i] Si deseas volver a ejecutarlo, simplemente utiliza este script nuevamente.")

# Punto de entrada del script
if __name__ == "__main__":
    main()