"""
Here I've written my version of implementation. So you can learn it.
Hope that you will find some interesting things.

Best regards!
"""


def get_max(a, b):
    """
    Returns max number among a and b.
    """

    return a if a > b else b


def get_max_without_arguments():
    """
    Raise TypeError exception with message as an argument.
    """

    raise TypeError("There is no argument, so it's not possible to find max value.")


def get_max_with_one_argument(a):
    """
    Returns that value.
    """

    return a


def get_max_with_many_arguments(*args):
    """
    Return the largest number among args.
    """

    max_number = float('-inf')

    for arg in args:
        if arg > max_number:
            max_number = arg

    return max_number


def get_max_with_one_or_more_arguments(first, *args):
    """
    Returns the largest number among first and args.
    """

    max_number = float('-inf')

    for arg in (first, *args):
        if arg > max_number:
            max_number = arg

    return max_number


def get_max_bounded(*args, low, high):
    """
    Returns the largest number among args bounded by low & high.
    """

    max_number = float('-inf')

    for arg in args:
        if arg > max_number and (low < arg and arg < high):
            max_number = arg

    return max_number


def make_max(*, low, high):
    """
    Returns an inner function object which takes at last one argument
    and return largest number amount it's arguments, but if the
    largest number is larger than the 'high' which given as required
    argument the inner function has to return it.
    """

    def inner(first, *args):
        max_number = float('-inf')

        for arg in (first, *args):
            if arg > max_number and (arg > low and arg < high):
                max_number = arg

        return max_number

    return inner
