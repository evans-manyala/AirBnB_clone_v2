#!/usr/bin/python3
"""
Application starts a Flask Application
"""

from flask import Flask
app = Flask(__name__)


# Define the path route to the root URL '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Return a string
    """
    return 'Hello HBNB!'


# Define the path route to '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Return "HBNB"
    """
    return 'HBNB'


# Define the path route to '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Return "C " followed by the value of the text variable
    Replace underscore _ symbols with a space
    """
    return f'C {text.replace("_", " ")}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
