@echo off
title Desinstalador Descargador MP3

echo Cerrando entorno virtual...
call venv\Scripts\deactivate.bat >nul 2>&1

echo Eliminando entorno virtual...
rmdir /s /q venv

echo Eliminando archivos temporales...
del /q /f *.spec
rmdir /s /q __pycache__
rmdir /s /q build
rmdir /s /q dist

echo Desinstalando librerías necesarias...
pip uninstall -y ffmpeg requests yt-dlp

:: Desinstalar Python (opcional)
:: echo Desinstalando Python...
:: wmic product where "name like 'Python%%'" call uninstall /nointeractive

echo Desinstalación completa.
pause
exit
