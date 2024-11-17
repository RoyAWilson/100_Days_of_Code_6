from typing import Literal
from flask import Flask
import random

app = Flask(__name__)

# Bold decorator


def bold_decorator(function):
    def wrapper(*args, **kwargs):
        return '<b>' + function() + '</b>'
    return wrapper


def italic_decorator(function):
    def wrapper(*args, **kwargs):
        return '<em>' + function() + '</em>'
    return wrapper


def underline_decorator(function):
    def wrapper(*args, **kwargs):
        return '<u>' + function() + '</u>'
    return wrapper


@app.route('/')
@app.route('/bye')
@bold_decorator
@italic_decorator
@underline_decorator
def bye():
    return 'Bye!'


if __name__ == '__main__':
    app.run(debug=True)
