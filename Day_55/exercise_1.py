def loggin_decorator(function):
    def wrapper(*args, **kwargs):
        print(function.__name__)
        print(function(*args))
    return wrapper


@loggin_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)
