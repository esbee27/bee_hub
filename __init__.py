#!/usr/bin/python3

"""a script that starts a Flask web application"""

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config('SECRET_KEY') = esbee27

    return app
@app.route('/', strict_slashes=False)
def hello():
    """Return a string"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)