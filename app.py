from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Función para buscar una palabra en la matriz
def find_word(matrix, word):
    rows, cols = len(matrix), len(matrix[0])
    directions = [
        (0, 1), (1, 0), (0, -1), (-1, 0),  # Horizontal y vertical
        (1, 1), (1, -1), (-1, 1), (-1, -1)  # Diagonales
    ]

    def search_direction(r, c, word, dr, dc):
        for i, char in enumerate(word):
            nr, nc = r + i * dr, c + i * dc
            if not (0 <= nr < rows and 0 <= nc < cols) or matrix[nr][nc] != char:
                return False
        return True

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == word[0]:  # Buscar la primera letra
                for dr, dc in directions:
                    if search_direction(r, c, word, dr, dc):
                        return True
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    # Convertir la matriz en una lista de listas
    matrix = [row.split(',') for row in data['matrix']]
    words = data['words']
    found, not_found = [], []

    # Buscar cada palabra
    for word in words:
        if find_word(matrix, word.strip().upper()):  # Buscar en mayúsculas
            found.append(word)
        else:
            not_found.append(word)

    # Retornar los resultados
    return jsonify({"found": found, "not_found": not_found})

if __name__ == '__main__':
    app.run(debug=True)
