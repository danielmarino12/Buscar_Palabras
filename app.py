from flask import Flask, render_template, request, jsonify
from PIL import Image
import pytesseract
import numpy as np
import cv2

app = Flask(__name__)

# Configura la ruta de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Función para buscar una palabra en la matriz y devolver sus coordenadas
def find_word(matrix, word):
    rows, cols = len(matrix), len(matrix[0])
    directions = [
        (0, 1), (1, 0), (0, -1), (-1, 0),  # Horizontal y vertical
        (1, 1), (1, -1), (-1, 1), (-1, -1)  # Diagonales
    ]

    def search_direction(r, c, word, dr, dc):
        path = []
        for i, char in enumerate(word):
            nr, nc = r + i * dr, c + i * dc
            if not (0 <= nr < rows and 0 <= nc < cols) or matrix[nr][nc] != char:
                return None
            path.append((nr, nc))
        return path

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == word[0]:  # Buscar la primera letra
                for dr, dc in directions:
                    path = search_direction(r, c, word, dr, dc)
                    if path:
                        return path
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    try:
        data = request.json
        if not data or 'matrix' not in data or 'words' not in data:
            return jsonify({"error": "Datos inválidos"}), 400

        matrix = [row.split(',') for row in data['matrix']]
        words = data['words']

        # Validar que todas las filas de la matriz tengan la misma longitud
        if len(set(len(row) for row in matrix)) != 1:
            return jsonify({"error": "Todas las filas deben tener el mismo número de columnas"}), 400

        found, not_found, coordinates = [], [], {}

        for word in words:
            path = find_word(matrix, word.strip().upper())  
            if path:
                found.append(word)
                coordinates[word] = path
            else:
                not_found.append(word)

        return jsonify({"found": found, "not_found": not_found, "coordinates": coordinates})
    except Exception as e:
        print("Error interno:", e)
        return jsonify({"error": "Error interno del servidor"}), 500

@app.route('/process-image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({"error": "No se envió ninguna imagen"}), 400

    image = request.files['image']
    try:
        # Abrir la imagen
        img = Image.open(image)
        img_cv = np.array(img)  # Convertir a formato de numpy array para usar con OpenCV
        
        # Preprocesar la imagen: convertir a escala de grises
        gray_img = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
        
        # Mejorar la imagen aplicando un umbral (threshold)
        _, thresh_img = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY)

        # Convertir la imagen preprocesada de nuevo a formato PIL para pytesseract
        pil_img = Image.fromarray(thresh_img)

        # Usar pytesseract con configuraciones adicionales para OCR
        custom_config = r'--oem 3 --psm 6'  # OCR Engine Mode (OEM) y Page Segmentation Mode (PSM)
        extracted_text = pytesseract.image_to_string(pil_img, config=custom_config)

        # Separar por filas y eliminar espacios extra
        rows = extracted_text.strip().split("\n")
        
        # Filtrar y procesar las filas
        processed_rows = []
        for row in rows:
            # Eliminar cualquier espacio en blanco extra y separar en caracteres
            chars = [char.upper() for char in row.strip() if char.isalpha()]  # Solo letras alfabéticas

            # Agregar comas hasta la 14ª letra, asegurándose de que cada fila tenga exactamente 14 caracteres
            if len(chars) > 14:
                processed_row = ",".join(chars[:14]) + "".join(chars[14:])
            else:
                processed_row = ",".join(chars) + "," * (14 - len(chars))  
            
            processed_rows.append(processed_row)

        # Convertir las filas procesadas de nuevo en una matriz
        matrix = "\n".join(processed_rows)
        
        return jsonify({"matrix": matrix})

    except Exception as e:
        print(f"Error procesando la imagen: {e}")
        return jsonify({"error": "Error procesando la imagen"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
