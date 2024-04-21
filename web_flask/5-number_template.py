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


# Define the path route to '/python'
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """
    Return "Python " followed by the value of the text variable
    Replace underscore _ symbols with a space
    """
    return f'Python {text.replace("_", " ")}'


# Define the path route to '/number/<int:n>'
@app.route('/number/<int:n>', strict_slashes=False)
def number_text(n):
    """
    Return "n is a number" if n is an integer
    """
    return f'{n} is a number'


# Define the path route to '/number_template/<int:n>'
@app.route('/number_template/<int:n>', strict_slashes=False)
def is_a_number_template(n=None):
    """Render a HTML page"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
