#!/usr/bin/python3

"""A script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)
"""app.config('SECRET_KEY') = esbee27"""

@app.route('/', strict_slashes=False)
def homePage():
    """Returns the homepage"""
    return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
