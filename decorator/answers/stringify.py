def stringify(func):
    """
    Takes a function as an argument and changes it's return type to string.

    :param func: decorated function

    :return inner function object
    :rtype function
    """

    def inner(*args):
        """
        Calls 'func' and convert it's result type into a string.
        """
        result = func(*args)
        return str(result)

    return inner


def add(a, b):
    """
    Decorated function which returns the sum of two numbers.
    """

    return a + b


add = stringify(add)


def multiply(a, b):
    """
    Decorated function which returns the multiplication of two numbers.
    """

    return a * b


multiply = stringify(multiply)
