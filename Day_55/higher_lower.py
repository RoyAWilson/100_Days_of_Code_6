from typing import Literal
from flask import Flask
import random

app = Flask(__name__)


def number():
    number = random.randint(1, 10)
    return number


def bld_h1_decorator(function):
    def wrapper(*args, **kwargs):
        return '<h1 style="color: red"><b><center>' + function(*args) + '</h1></b></center>'
    return wrapper


@app.route('/')
@bld_h1_decorator
def landing_page():
    return 'Guess A Number Between 0 And 9<br><img src="https://media3.giphy.com/media/IsfrRWvbUdRny/200.webp?cid=ecf05e47an7f0lq9vqt4jjbrz981foo9vudi9fd7uv7q8f4s&ep=v1_gifs_search&rid=200.webp&ct=g">'


g_number = number()


@app.route('/<int:guess>')
def guess_page(guess):

    if guess == g_number:
        return '<h1 style="color: green"><b><center>Congratulations You Guessed Right</b></h1></center>\
            <center><img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXR4NjhndWJmc3poa3pmeTJ3cnl0aThiaDI3ZHE4NzRjdHNxNW5uMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/FTLnswEmDh8xBgIXdE/giphy.webp"></center>'
    elif guess < g_number:
        return '<h1 style="color: brown"><b1><center>You guessed too low</b></h1>\
            <center><img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmVvNHUwNzRvemFyNDF1NDZ6emcxanFnd3kydnQwZzdodnN3dDkzNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TgmiJ4AZ3HSiIqpOj6/giphy.webp"></center>'
    elif guess > g_number:
        return '<h1 style = "color: blue"><b1><center>You guessed too high</b></h1><center><img src="https://i.giphy.com/YKroe55zFMIwpmBCu6.webp"></center>'


if __name__ == '__main__':
    # to_guess = number()

    app.run(debug=True)
