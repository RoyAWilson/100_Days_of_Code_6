# Python decorator function intro

import time


def delay_decorator(function):
    def my_wrapper():
        time.sleep(2)
        function()
    return my_wrapper


@delay_decorator
def say_hello() -> None:
    print('Hello')


@delay_decorator
def say_bye() -> None:
    print('Goodbye!')


def greeting() -> None:
    print('How are you?')


say_hello()
greeting()
say_bye()

decorated_funct = delay_decorator(greeting)
decorated_funct()
