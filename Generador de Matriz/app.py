from flask import Flask, render_template, request
import random
import requests

app = Flask(__name__)

# Función para obtener palabras usando la API de Datamuse
def get_related_words(theme):
    url = f"https://api.datamuse.com/words?rel_trg={theme}&max=10"
    response = requests.get(url)
    words = [word['word'].upper() for word in response.json()]  # Asegurar mayúsculas
    return words

# Funciones para generar la matriz de búsqueda
def generate_empty_matrix(size=14):
    return [[' ' for _ in range(size)] for _ in range(size)]

def add_word_to_matrix(matrix, word, direction, row, col):
    word_len = len(word)
    if direction == "horizontal":
        for i in range(word_len):
            matrix[row][col + i] = word[i]
    elif direction == "vertical":
        for i in range(word_len):
            matrix[row + i][col] = word[i]
    elif direction == "diagonal_down":
        for i in range(word_len):
            matrix[row + i][col + i] = word[i]
    elif direction == "diagonal_up":
        for i in range(word_len):
            matrix[row - i][col + i] = word[i]

def can_place_word(matrix, word, direction, row, col):
    word_len = len(word)
    if direction == "horizontal" and col + word_len <= len(matrix[0]):
        return all(matrix[row][col + i] == ' ' or matrix[row][col + i] == word[i] for i in range(word_len))
    elif direction == "vertical" and row + word_len <= len(matrix):
        return all(matrix[row + i][col] == ' ' or matrix[row + i][col] == word[i] for i in range(word_len))
    elif direction == "diagonal_down" and row + word_len <= len(matrix) and col + word_len <= len(matrix[0]):
        return all(matrix[row + i][col + i] == ' ' or matrix[row + i][col + i] == word[i] for i in range(word_len))
    elif direction == "diagonal_up" and row - word_len >= -1 and col + word_len <= len(matrix[0]):
        return all(matrix[row - i][col + i] == ' ' or matrix[row - i][col + i] == word[i] for i in range(word_len))
    return False

def add_words_to_matrix(matrix, words):
    for word in words:
        placed = False
        while not placed:
            direction = random.choice(["horizontal", "vertical", "diagonal_down", "diagonal_up"])
            row = random.randint(0, len(matrix) - 1)
            col = random.randint(0, len(matrix[0]) - 1)
            if can_place_word(matrix, word, direction, row, col):
                add_word_to_matrix(matrix, word, direction, row, col)
                placed = True

def fill_random_letters(matrix):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == ' ':
                matrix[i][j] = random.choice(letters)

def generate_word_search(words, size=14):
    matrix = generate_empty_matrix(size)
    add_words_to_matrix(matrix, words)
    fill_random_letters(matrix)
    return matrix

# Convertir matriz a texto limpio
def matrix_to_text(matrix):
    return [''.join(row) for row in matrix]

# Ruta para generar la matriz
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "theme" in request.form:
            theme = request.form.get("theme")
            words = get_related_words(theme)  # Obtener palabras de la API
            if not words:
                return render_template("index.html", error="No se encontraron palabras para este tema.")
            matrix = generate_word_search(words)
            matrix_text = matrix_to_text(matrix)  
            return render_template("index.html", matrix=matrix_text, words=words, theme=theme)
    return render_template("index.html", matrix=None)

if __name__ == "__main__":
    app.run(debug=True, port=5001) 
