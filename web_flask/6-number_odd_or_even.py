#!/usr/bin/python3
"""
Application starts a Flask Application
"""

from flask import Flask, render_template
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
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


# Define the path route to '/number_template/<int:n>'
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


# Define the path route to '/number_odd_or_even/<int:n>'
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        odd_even = 'even'
    else:
        odd_even = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, odd_even=odd_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
