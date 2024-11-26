@echo off
REM Cambiar a la carpeta del proyecto
cd %~dp0

REM Comprobar si Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python no está instalado. Por favor, instala Python y vuelve a intentarlo.
    pause
    exit /b
)

REM Crear el entorno virtual si no existe
if not exist venv (
    echo Creando entorno virtual...
    python -m venv venv
)

REM Activar el entorno virtual
call venv\Scripts\activate

REM Instalar los paquetes desde requirements.txt
if exist requirements.txt (
    echo Instalando dependencias...
    pip install -r requirements.txt
) else (
    echo No se encontró el archivo requirements.txt. Asegúrate de incluirlo.
    pause
    exit /b
)

REM Confirmar que el proceso se completó
echo Entorno virtual configurado y dependencias instaladas correctamente.
pause
