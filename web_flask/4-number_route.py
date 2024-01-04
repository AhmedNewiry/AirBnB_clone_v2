#!/usr/bin/python3
"""A script that starts a flask web application"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """displays hello message"""
    return 'Hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text_route(text):
    """displays 'C' followed by
       the text variable value
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def text_py_route(text='is cool'):
    """displays 'Python' followed by
       the text variable value
    """
    text = text.replace('_', ' ')
    return 'Pyhton {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """displays 'n' is a number
       only if n is an integer
    """
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
