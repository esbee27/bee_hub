#!/usr/bin/python3

"""A script that starts a Flask web application"""

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config('SECRET_KEY') = esbee27

    return app
@app.route('/', strict_slashes=False)
def homePage():
    """Returns the homepage"""
    return "home.html"

@app.route('/login', strict_slashes=False)
def login():
    """Returns the login page"""
    return "login.html"

@app.route('signup')
def signUp():
    """Returns the sign up page"""
    return "signUp.html"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)