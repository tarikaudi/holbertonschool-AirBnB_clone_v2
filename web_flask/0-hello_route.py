#!/usr/bin/python3
"""comment for the check"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def lobby():
    """def home fun"""
    return ("Hello HBNB!")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
