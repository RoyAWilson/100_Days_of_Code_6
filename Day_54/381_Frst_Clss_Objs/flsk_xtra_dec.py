from typing import Literal
from flask import Flask
import random

app = Flask(__name__)

print(random.__name__)
print(__name__)


@app.route('/')
def hello_world() -> Literal['<p>Hello World!</p)']:
    return '<p>Hello World!</p)'


@app.route('/bye')
def say_bye():
    return "Bye!"


if __name__ == '__main__':
    app.run()
