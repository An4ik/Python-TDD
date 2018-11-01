def get_min(a, b):
    """
    Returns min number among a and b
    """

    return a if a < b else b


def get_min_without_arguments():
    """
    Raises TypeError exception with message.
    """

    raise TypeError("No argument error.")


def get_min_with_one_argument(x):
    """
    Returns that value.
    """

    return x


def get_min_with_many_arguments(*args):
    """
    Returns the smallest number among args.
    """

    min_number = float('inf')

    for arg in args:
        if arg < min_number:
            min_number = arg

    return min_number


def get_min_with_one_or_more_arguments(first, *args):
    """
    Returns the smallest number among first + args.
    """

    min_number = float('inf')

    for arg in (first, *args):
        if arg < min_number:
            min_number = arg

    return min_number


def get_min_bounded(*args, low, high):
    """
    Returns the smallest number among args bounded by low & high.
    """

    min_number = float('Inf')

    for arg in args:
        if arg < min_number and (low < arg and arg < high):
            min_number = arg

    return min_number


def make_min(*, low, high):
    """
    Returns an inner function object which takes at last one argument
    and return smallest number amount it's arguments, but if the
    smallest number is lower than the 'low' which given as required
    argument the inner function has to return it.
    """

    def inner(first, *args):
        min_number = float('inf')

        for arg in (first, *args):
            if arg < min_number and (arg > low and arg < high):
                min_number = arg

        return min_number

    return inner
