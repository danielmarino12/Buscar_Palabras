from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    
    return jsonify({"message": "Prueba de Conexcion"})

if __name__ == '__main__':
    app.run(debug=True)
