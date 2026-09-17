from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Register a basic route that is not implemented yet
@app.route('/hello')
def hello():
    return "Hello, World!"
