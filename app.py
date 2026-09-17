from flask import Flask, jsonify, request
from calculator import add, subtract, multiply, divide

# Initialize the Flask application
app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello, World!"

@app.route('/calc', methods=['GET'])
def calc():
    operation = request.args.get('op')
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))

    if operation == 'add':
        result = add(x, y)
    elif operation == 'subtract':
        result = subtract(x, y)
    elif operation == 'multiply':
        result = multiply(x, y)
    elif operation == 'divide':
        result = divide(x, y)
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({"result": result})
