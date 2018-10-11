

def get_min(a, b):
    """
        return min number among a and b
    """

    if a < b:
        return a
    else:
        return b


def get_min_without_arguments():
    """
        raise TypeError exception with message
    """

    raise TypeError("No argument error")


def get_min_with_one_argument(x):
    """
        return that value
    """

    return x


def get_min_with_many_arguments(*args):
    """
        return smallest number among args
    """

    minNumber = float('inf')

    for arg in args:
        if arg < minNumber:
            minNumber = arg

    return minNumber


def get_min_with_one_or_more_arguments(first, *args):
    """
        return smallest number among first + args
    """

    minNumber = float('inf')

    for arg in (first, *args):
        if arg < minNumber:
            minNumber = arg

    return minNumber

def get_min_bounded(*args, low, high):
    """
        return smallest number among args bounded by low & high
    """

    minNumber = float('Inf')

    for arg in args:
        if arg < minNumber and (low < arg and arg < high):
            minNumber = arg

    return minNumber



def make_min(*, low, high):
    """
        return inner function object which takes at last one argument
        and return smallest number amount it's arguments, but if the
        smallest number is lower than the 'low' which given as required
        argument the inner function has to return it.
    """

    def inner(first, *args):
        minNumber = float('inf')

        for arg in (first, *args):
            if arg < minNumber and (arg > low and arg < high):
                minNumber = arg
        return minNumber

    return inner
