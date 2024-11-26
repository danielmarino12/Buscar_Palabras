@echo off
REM Activa el entorno virtual
cd C:\Users\Pc\Desktop\Busca_Palabras
call env\Scripts\activate

REM Inicia el servidor principal en puerto 5000
start /min cmd /k "python app.py"

REM Cambia al directorio del generador de matrices
cd "C:\Users\Pc\Desktop\Busca_Palabras\Generador de Matriz"

REM Inicia el servidor del generador de matrices en puerto 5001
start /min cmd /k "python app.py"

REM Espera unos segundos para que los servidores se inicien
timeout /t 5 > nul

REM Abre el navegador en el servidor 5000
start http://127.0.0.1:5000
