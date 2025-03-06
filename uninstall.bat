@echo off
title Desinstalador de Descargador MP3
setlocal EnableDelayedExpansion

:: Spinner
set "spin=-\|/"
set "i=0"

:: Función para mostrar animación mientras se ejecutan comandos
:spinner
set /a "i=(i+1)%%4"
<nul set /p "=Eliminando... !spin:~%i,1! "
timeout /t 1 /nobreak >nul
exit /b

:: Animación mientras eliminamos algo
call :spinner

echo.
echo 🔻 Cerrando entorno virtual (si está activo)...
if exist venv\Scripts\activate.bat (
    call venv\Scripts\deactivate.bat >nul 2>&1
)
call :spinner

echo.
echo 🗑️ Eliminando entorno virtual...
rmdir /s /q venv
call :spinner

echo.
echo 🗑️ Eliminando archivos temporales...
del /q /f *.spec
rmdir /s /q __pycache__
rmdir /s /q build
rmdir /s /q dist
call :spinner

echo.
echo 🗑️ Eliminando FFmpeg si fue instalado...
if exist C:\ffmpeg (
    rmdir /s /q C:\ffmpeg
    echo ✅ FFmpeg eliminado.
)
call :spinner

echo.
echo 🗑️ Eliminando archivo ZIP de FFmpeg (si existe)...
if exist ffmpeg.zip del /q /f ffmpeg.zip
call :spinner

echo.
echo 🔽 Desinstalando librerías globales (si es necesario)...
pip uninstall -y ffmpeg requests yt-dlp
call :spinner

:: Desinstalar Python (opcional)
:: echo 🗑️ Desinstalando Python...
:: wmic product where "name like 'Python%%'" call uninstall /nointeractive
:: call :spinner

echo.
echo ✅ Desinstalación completa.
pause
exit
