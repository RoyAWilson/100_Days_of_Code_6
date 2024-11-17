'''
Examine passing functions to functions:
'''


def add(n1: float, n2: float) -> float:
    """_summary_
    To add 2 floats
    Args:
        n1 (float): first float in addition
        n2 (float): second float in addition

    Returns:
        float: Sum of the two floats passed
    """

    return n1 + n2


def subtract(n1: float, n2: float) -> float:
    """_summary_
    To subtract float 1 from float 2
    Args:
        n1 (float): float from which to subtract
        n2 (float): float to subtract from n1

    Returns:
        float: n1 - n2
    """
    return n1 - n2


def divide(n1: float, n2: float) -> float:
    """_summary_
    Return float of n1 divided by n2
    Args:
        n1 (float): enumerator
        n2 (float): denominator

    Returns:
        float: division of n1 by n2
    """
    return n1 / n2


def multiply(n1: float, n2: float) -> float:
    """Return product of n1 * n2 as float

    Args:
        n1 (float): first number in mutliplication
        n2 (float): second number in multiplication

    Returns:
        float: _description_
    """
    return n1 * n2


def calculate(calc_func, n1: float, n2: float) -> float:
    """returns calculation using passed function and floats passed

    Args:
        calc_func (function): one of the arithemetic functions: add, subtract, divide, multiply
        n1 (float): first number to pass to calculation
        n2 (_type_): Second number to pass to calculation

    Returns:
        float: calculated return using n1 and n2
    """
    return calc_func(n1, n2)


print(calculate(multiply, 20, 2))
print(calculate(add, 12, 75))

# Nested functions:


'''def outer_func():
    print('I am outer function')

    def inner_func() -> None:
        print('I am nested function')

    inner_func()


outer_func()'''

# Functions returning other functions


def outer_func():
    print('I am outer function')

    def inner_func() -> None:
        print('I am nested function')

    return inner_func


# outer_func()
in_func = outer_func()
in_func()
