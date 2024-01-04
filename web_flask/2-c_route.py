#!/usr/bin/python3
"""A script that starts a flask web application"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """displays hello message"""
    return 'Hello HBNB!'


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
