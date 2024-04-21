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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
