# 🎵 Descargador de MP3 con Portada (Instalación Manual - Windows) 🎵
Este es un script hecho en Python que permite descargar música de YouTube en formato MP3, incluyendo la portada del video. 🎧

## 📥 Instalación
1️⃣ Instalación de Python
Si no tienes instalado Python, primero debes instalarlo para poder usar este script. Ve a la página oficial de Python y descarga la versión más estable:
[Descarga_Python](https://www.python.org/downloads/)

Una vez descargado, ejecuta el instalador y sigue los pasos de instalación.

**Recomendación Forzosa:**
Durante la instalación, activa las siguientes casillas para evitar problemas más adelante:
✅ "Use admin privileges when installing py.exe"
✅ "Add python.exe to PATH"

Luego, espera a que finalice la instalación.
Si ya tienes instalado Python, puedes saltarte este paso.

2️⃣ Instalación de dependencias
Ahora instalaremos las dependencias necesarias para que el script funcione.

🔹 Paso 1: Abre una terminal en Windows:

Presiona Win + R, escribe cmd y presiona Enter.
🔹 Paso 2: Ejecuta los siguientes comandos en la terminal:

📌 Comando 1: Instalar las librerías necesarias:

```
pip install yt-dlp requests
```

📌 Comando 2: Instalar FFmpeg para procesar los archivos de audio:

```
winget install ffmpeg --accept-package-agreements --accept-source-agreements -h
```
Espera a que finalicen las instalaciones.

3️⃣ Todo listo, ¡instalación completada! 🎉
Ahora solo descarga el archivo ZIP de este repositorio, descomprímelo y mueve la carpeta del script a donde más te guste.

## 🚀 Uso
🔹 Paso 1: Entra en la carpeta que descomprimiste y encontrarás los siguientes archivos:

```
 download_mp3.py
 README.md
```
🔹 Paso 2: Abre una terminal dentro de esta carpeta:

**Mantén presionada la tecla Shift + haz clic derecho en la carpeta.**
**Selecciona la opción "Abrir en terminal".**
🔹 Paso 3: Ejecuta el script:
Ejecuta el siguiente comando:
```
python download_mp3.py
```
El script te pedirá que ingreses la URL de la canción que deseas descargar.
Presiona Enter y tu música se descargará en la carpeta "musica". 🎶

## 📌 Recomendaciones
🔹 Descargar playlists completas
También puedes descargar una lista de reproducción completa. Solo ingresa el link de la playlist y espera a que termine. Esto también funciona para álbumes completos que estén en formato de playlist.

## 📝 Nota
Por ahora, este proyecto solo funciona en Windows. Si tienes experiencia con otros sistemas operativos como Linux o MacOS, puedes adaptarlo fácilmente.

Actualmente, el proyecto está en desarrollo. Se espera agregar compatibilidad con Linux y MacOS y la posibilidad de descargar videos en futuras actualizaciones.

El objetivo es crear una herramienta gratuita, fácil de usar y confiable.

💻 Desarrollado por 👉: 
> by https://github.com/aleatomic 