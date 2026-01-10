#Importamos las librerias necesarias
import os #Para manejar archivos y directorios
import subprocess #Para ejecutar comandos en la terminal
import zipfile #Para extraer archivos ZIP
import requests #Para descargar archivos desde internet de ser necesario

FFMPEG_URL = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-n6.1-latest-win64-gpl.zip"
INSTALL_PATH = "C:\\ffmpeg"
BIN_PATH = os.path.join(INSTALL_PATH, "bin") # Ruta de la carpeta "bin" de FFmpeg, donde contiene los ejecutables

#Funcion 
def is_ffmpeg_installed():
    """Verifica si FFmpeg está instalado ejecutando 'ffmpeg -version'."""
    #Intentamos ejecutar el comando ffmpeg -version, si no funciona, devolvemos False, y significa que no está instalado
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print("✅ FFmpeg ya está instalado.")
        return True
    except FileNotFoundError:
        return False

# Funcion para descargar FFmpeg
def download_ffmpeg():
    """Descarga FFmpeg desde el enlace especificado."""
    print("🔽 Descargando FFmpeg...")
    response = requests.get(FFMPEG_URL, stream=True) # usa stream=True para descargar grandes archivos
    zip_path = "ffmpeg.zip"

    with open(zip_path, "wb") as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)

    print("✅ Descarga completada.")
    return zip_path

# Funcion para extraer FFmpeg
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

# Funcion para agregar FFmpeg al PATH
def add_to_path():
    """Agrega FFmpeg a las variables de entorno del sistema."""
    print("🛠️ Configurando FFmpeg en PATH...")

    path_var = os.environ.get("PATH", "")
    
    #Verificamos si la carpeta "bin" de FFmpeg ya está en PATH o no
    if BIN_PATH not in path_var:
        subprocess.run(f'setx PATH "{path_var};{BIN_PATH}"', shell=True)
        print("✅ FFmpeg agregado al PATH. Reinicia la terminal para aplicar cambios.")
    else:
        print("⚠️ FFmpeg ya está en PATH.")

# Funcion principal
def main():
    # Revisamos si FFmpeg ya está instalado, si no, lo descargamos
    if not is_ffmpeg_installed():
        zip_path = download_ffmpeg()
        extract_ffmpeg(zip_path)
        add_to_path()
        print("🎉 Instalación completada. Reinicia tu terminal para aplicar los cambios.")
    else:
        # Si FFmpeg ya está instalado, no hacemos nada
        print("👌 No es necesario instalar FFmpeg.")

# Permite que el script se ejecute desde la terminal, si este es importado en otro archivo, no se ejecutará
if __name__ == "__main__":
    main()

"""
Que es FFmpeg y por qué lo necesitamos?
FFmpeg es una herramienta de línea de comandos muy poderosa y versátil para procesar multimedia, es decir, trabajar con archivos de audio, 
video e incluso imágenes. Se trata de una biblioteca y un conjunto de programas que permite grabar, convertir y transmitir archivos de audio y 
video en múltiples formatos.
Es de codigo abierto.

Lo usaremos en el proyecto para convertir archivos de audio y poner la pprtada:
1.- Es posible que los archivos de audio descargados no estén en el formato MP3 por defecto. FFmpeg permite convertir esos archivos a MP3, que 
es uno de los formatos más populares y ampliamente utilizados para almacenar música.
2.- FFmpeg también se puede usar para agregar la imagen de la portada (que podrías descargar junto con la música) al archivo MP3.
El proceso de integrar la imagen de portada en el archivo MP3 (como metadato) se realiza para que la música tenga una carátula cuando se 
reproduzca en un reproductor de música.

"""
