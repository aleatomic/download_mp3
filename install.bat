:: Ocultamos los comandos de la terminal, para que solo se muestren los mensajes
@echo off
:: Se modifica el titulo de la ventana
title Instalador de Descargador de MP3 by github.com/aleatomic
echo ----------------------------------------
echo  Instalando Descargador de MP3
echo ----------------------------------------

:: Verificar si Python está instalado
:: Verificacion para saber si python esta en PATH, si el comando falla, significa que no está instalado, por lo tanto se descarga una version de python
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Python no está instalado. Descargándolo...
    :: Descargar Python
    ::bitsadmin /transfer "Descargando Python" https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe python_installer.exe
    ::call :spinner "bitsadmin /transfer 'Descargando Python' https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe python_installer.exe"
    :: Se usa para descargar cosas de internet desde la terminal                   URL                               Nombre con el que se guarda el archivo
    call :spinner "bitsadmin /transfer 'Descargando Python' https://www.python.org/ftp/python/3.13.2/python-3.13.2-amd64.exe python_installer.exe"
    
    echo 🛠️ Instalando Python...
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
    
    ::echo ✅ Python instalado correctamente. Eliminando el instalador...
    ::del python_installer.exe
    echo ✅ Python instalado correctamente.
)

:: Creamos un entorno virtual para mantener limpio el equipo del usuario, y no afectar configuracion que este peuda tener
:: Crear entorno virtual (opcional)
echo 🔽 Creando entorno virtual...
::python -m venv env
call :spinner "python -m venv env"
:: Activar entorno virtual
call env\Scripts\activate

:: Instalar paquetes necesarios, instala las librerias desde el archivo requirements.txt
echo 🔽 Instalando dependencias de Python...
::pip install -r requirements.txt
call :spinner "pip install -r requirements.txt"

:: Ejecutar script de instalación
echo 🛠️ Configurando FFmpeg...
::python install_depency.py
call :spinner "python install_depency.py"

echo ✅ Instalación completada. Usa 'python download_mp3.py' para empezar.
:: Esperamos a que el usuario presione una tecla antes de cerrar la ventana
pause
:: Cerramos la ventana
exit

:: ==================== FUNCION SPINNER ====================
:spinner
setlocal EnableDelayedExpansion
:: Asigna el primer argumento a la funcion spinner a la variable cmd. El ~ elimina comillas alrededor del argumento
set "cmd=%~1"
:: Se crea un string con los caracteres de la variable spin
set "spin=\|/-"
:: Se crea un bucle infinito
for /l %%n in () do (
    :: Bucle para recorrer los caracteres de la variable spin
    for /l %%i in (0,1,3) do (
        :: Puede que ^H^H^H no funcione correctamente en todas las terminales y puede que no se logre el efecto deseado
        <nul set /p "=Procesando... !spin:~%%i,1! ^H^H^H" 
        %cmd% >nul 2>&1 && exit /b
        timeout /t 1 >nul
    )
)
exit /b