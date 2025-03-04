import os
import subprocess
import zipfile
import requests

FFMPEG_URL = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-n6.1-latest-win64-gpl.zip"
INSTALL_PATH = "C:\\ffmpeg"
BIN_PATH = os.path.join(INSTALL_PATH, "bin")

def is_ffmpeg_installed():
    """Verifica si FFmpeg está instalado ejecutando 'ffmpeg -version'."""
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print("✅ FFmpeg ya está instalado.")
        return True
    except FileNotFoundError:
        return False

def download_ffmpeg():
    """Descarga FFmpeg desde el enlace especificado."""
    print("🔽 Descargando FFmpeg...")
    response = requests.get(FFMPEG_URL, stream=True)
    zip_path = "ffmpeg.zip"

    with open(zip_path, "wb") as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)

    print("✅ Descarga completada.")
    return zip_path

def extract_ffmpeg(zip_path):
    """Extrae FFmpeg en la ruta de instalación."""
    print("📂 Extrayendo archivos...")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(INSTALL_PATH)

    # La carpeta extraída tiene un nombre largo, movemos solo el contenido de "bin"
    extracted_folder = os.path.join(INSTALL_PATH, os.listdir(INSTALL_PATH)[0], "bin")
    
    # Si la carpeta "bin" no existe, movemos los archivos correctos
    if not os.path.exists(BIN_PATH):
        os.rename(extracted_folder, BIN_PATH)

    os.remove(zip_path)  # Eliminar el ZIP descargado
    print("✅ Extracción completada.")

def add_to_path():
    """Agrega FFmpeg a las variables de entorno del sistema."""
    print("🛠️ Configurando FFmpeg en PATH...")

    path_var = os.environ.get("PATH", "")
    
    if BIN_PATH not in path_var:
        subprocess.run(f'setx PATH "{path_var};{BIN_PATH}"', shell=True)
        print("✅ FFmpeg agregado al PATH. Reinicia la terminal para aplicar cambios.")
    else:
        print("⚠️ FFmpeg ya está en PATH.")

def main():
    if not is_ffmpeg_installed():
        zip_path = download_ffmpeg()
        extract_ffmpeg(zip_path)
        add_to_path()
        print("🎉 Instalación completada. Reinicia tu terminal para aplicar los cambios.")
    else:
        print("👌 No es necesario instalar FFmpeg.")

if __name__ == "__main__":
    main()
