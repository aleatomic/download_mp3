@echo off
title Instalador de Descargador de MP3 by atomic
echo ----------------------------------------
echo  Instalando Descargador de MP3
echo ----------------------------------------

:: Verificar si Python está instalado
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Python no está instalado. Descargándolo...
    start "" "https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe"
    echo 🛠️ Instala Python manualmente y ejecuta este script nuevamente.
    exit
)

:: Crear entorno virtual (opcional)
echo 🔽 Creando entorno virtual...
python -m venv env
call env\Scripts\activate

:: Instalar paquetes necesarios
echo 🔽 Instalando dependencias de Python...
pip install -r requirements.txt

:: Ejecutar script de instalación
echo 🛠️ Configurando FFmpeg...
python install_depency.py

echo ✅ Instalación completada. Usa 'python download_mp3.py' para empezar.
pause
exit
