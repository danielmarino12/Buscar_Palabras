# Buscador de Palabras y Gestor de Matrices

Este proyecto consta de dos aplicaciones principales: un Buscador de Palabras y un Gestor de Matrices. El Buscador de Palabras permite a los usuarios buscar palabras dentro de una matriz de texto proporcionada, o generada desde una imagen esta extrae texto de imágenes (como matrices) utilizando OCR (Reconocimiento Óptico de Caracteres) y luego permite realizar búsquedas en el texto extraído, en cambio el generador de matriz  toma una palabra de entrada y genera una matriz de caracteres alrededor de esa palabra, colocando la palabra en la matriz y rellenando el resto con caracteres aleatorios, se realiza por medio de una api.

## Tecnologias Utilizadas

Python 3.11: Lenguaje de programación principal. <img height="50" src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png">

pytesseract: Herramienta para realizar OCR sobre imágenes (para el caso de imágenes con texto).

OpenCV: Biblioteca para el procesamiento de imágenes antes de aplicar OCR.

Requests: Biblioteca de Python utilizada para realizar solicitudes HTTP a otros servicios.

Flask: Framework web utilizado para crear los servidores backend de ambos proyectos. <img height="50" src="https://user-images.githubusercontent.com/25181517/183423775-2276e25d-d43d-4e58-890b-edbc88e915f7.png">

JavaScript: Leguaje por funciones en la web. <img height="50" src="https://user-images.githubusercontent.com/25181517/117447155-6a868a00-af3d-11eb-9cfe-245df15c9f3f.png">


HTML, CSS: Para la creación de la interfaz de usuario (Frontend).<img height="50" src="https://user-images.githubusercontent.com/25181517/192158954-f88b5814-d510-4564-b285-dff7d6400dad.png"> <img height="50" src="https://user-images.githubusercontent.com/25181517/183898674-75a4a1b1-f960-4ea9-abcb-637170a00a75.png">

Virtualenv: Para gestionar las dependencias del proyecto en un entorno virtual



## Instalación
1.	Crear Carpeta en el escritorio: Crear una carpeta en el escritorio Llamada Busca_Palabras.

2.	Instalar Python: Instalar Python versión 3.11

3.	Instalar Tesseract OCR: Debes instalar Tesseract en tu sistema para poder extraer texto de imágenes (Instalador incluido en los archivos de GITHUB).

4.	Copia lo archivos: Copia los archivos descargados del GITHUB en la carpeta Busca_Palabras.

5.	Crear entorno virtual e instalar requerimientos: Tienes dos formas de crear el entorno, activarlo e instalar los requerimientos:

- Ejecutando archivo .bat: Solo debes darle doble clic al archivo execute.bat él lo que hará es comprobar si tienes Python   instalado, creara el entrono virtual, lo activara e instalara los requerimientos necesarios para la ejecución del proyecto.

- Ejecutando por consola: Solo debes desde cualquier consola navegar hasta la carpeta del proyecto, estando ahí pones este comando python -m venv env esperas que termine e ingresas a esta ruta env\Scripts\activate y regresas a la ruta de la carpeta. Aquí ya puedes instalar los requerimientos con este comando pip install -r requirements.txt y listo esperas que termine y ya puedes pasar al siguiente paso.
Crear y activar entorno virtual

```bash
python -m venv env
env\Scripts\activate
```

6.	Modifica las rutas: Modifica las rutas de archivo del archivo starts_servers.bat, esto lo puedes hacer dándole clic derecho al archivo y editar ahí solo debes modificar solo el usuario: C:\Users\pones tu usuario\Desktop\Busca_Palabras eso lo debes de hacer en las rutas que encuentres en él .bat que exactamente son 2, por último, guardas los cambios.
```bash
 C:\Users\pones tu usuario\Desktop\Busca_Palabras
```
8.	Ejecutar el .bat: Después de modificado y guardado el archivo .bat ejecutas el archivo dándole doble clic y el iniciara los servidores y te abre el navegador con el aplicativo web.

## Uso
### Buscar Palabras con Matriz copiada
1. Abrir en el navegador
```bash
http://127.0.0.1:5000/
```
2. Ingresa la matriz generada (como una cuadrícula de letras 14x14).
```bash
C,E,N,T,I,M,E,T,E,R,C,S,E,S
F,G,J,V,W,V,W,L,E,G,U,M,E,Z
P,S,F,P,N,F,M,E,J,V,E,I,F,X
R,A,Y,L,M,I,M,X,T,N,R,W,T,E
S,I,Y,S,W,Y,O,I,E,R,A,R,P,L
R,F,P,Z,B,I,E,H,E,A,H,I,A,X
S,I,T,E,K,Z,C,H,Q,W,O,P,W,U
M,A,P,Q,N,A,C,G,D,Y,Y,E,Q,Z
A,A,J,E,M,I,H,P,A,P,P,U,S,S
T,H,W,P,N,J,N,F,X,P,H,J,Y,Z
U,D,D,R,U,P,E,G,Z,Z,H,R,H,K
R,E,N,O,L,Q,V,G,Q,T,T,T,R,O
E,O,R,B,T,J,Z,Z,D,N,O,J,F,C
S,I,X,V,N,O,V,M,V,G,O,Y,I,O
``` 
3. Escribe las palabras que deseas buscar, separadas por comas.
4. Haz clic en Buscar Palabras para buscar las palabras en la matriz.

5. Los resultados te mostrarán las palabras encontradas y no encontradas y podrá descargar las palabras y sus coordenadas en un archivo json.

### Procesar imagen para sacar matriz
1. En la misma interfaz en el botón procesar imagen

2. Seleccionar una imagen con la estructura correspondiente (14x14)
3. Dar clic en botón extraer matriz y se genera una matriz extrayendo las letras de la imagen, la cual copia y pega en la anterior interfaz agregando las palabras a buscar.

### Generador de Matrices
1. Botón a gestor de matrices
2. En la nueva pagina va a solicitar una palabra la cual debe ser en ingles (cars) y el automáticamente generara una matriz 14x14 con palabras que tengan que ver con la palabra buscada(nissan, renault, etc), poniéndolas en forma vertical, horizontal y diagonal, y genera también las palabras insertadas en la matriz para que la pruebes en el buscador de palabras.

### Nota: Manual incluido en el repositorio
