#!/usr/bin/python3
"""comment for the check"""


from flask import Flask
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
def c_is_etc(text):
    """parse text __"""
    parse_text = text.replace('_', ' ')
    return "{}".format(parse_text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
