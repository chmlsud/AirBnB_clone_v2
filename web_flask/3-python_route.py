#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function call """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Function call """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Function call /c/<text> route """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """ Function call /python/<text> """
    if text is not 'is cool':
        text = text.replace('_', ' ')
    return 'Python %s' % text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
