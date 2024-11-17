from typing import Literal
from flask import Flask
import random

app = Flask(__name__)

print(random.__name__)
print(__name__)


@app.route('/')
def hello_world() -> Literal['<p>Hello World!</p)']:
    return '<h1 style="text-align: center">Hello World!</h1>\
        <p>This is a paragraph</p>\
            <p><img src="https://i.guim.co.uk/img/media/43352be36da0eb156e8551d775a57fadba8ae6d7/0_0_1440_864/master/1440.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=1829611852af3ffc6460b4068e20bcbc"\
                width=300></p><p><img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTk3NHozcmtiMXR6ZGxiZHRvMGxnY3lreHY2ZWhtamhvcjM1MjVodiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qFxlqjtA3m44U/200.webp"\
                    width=300></p>'


@app.route('/bye')
def bye():
    return '<p>Bye!<p>'


@app.route('/username/<name>')
def greet_name(name):
    return f'<p>Hello {name}! how are you?<p> '


@app.route('/user/<fname>/<int:number>')
def greet_name_age(fname, number):
    return f'<p>Hello {fname}! you are <b>{number}</b> years old<p> '


if __name__ == '__main__':
    app.run(debug=True)
