#!/usr/bin/python3
"""comment for the check"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def lobby():
    """def lobby fun"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def home():
    """def home fun"""
    return ("HBNB")

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """parse text __"""
    parse_text = text.replace('_', ' ')
    return "{}".format(parse_text)

@app.route('/python')
@app.route('/python/<text>', strict_slashes=False)
def python_etc(text="is cool"):
    """python etc fun"""
    return ("Python {}".format(text.replace('_', ' ')))

@app.route('/number/<int:n>', strict_slashes=False)
def is_int(n):
    """is int fun"""
    return ("{} is a number".format(n))

@app.route('/number_template/<int:n>', strict_slashes=False)
def link(n):
    """link with template"""
    return (render_template('5-number.html', n=n))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
