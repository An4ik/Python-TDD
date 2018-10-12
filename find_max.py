def get_max(a, b):
    """
        return max number among a and b
    """
    if (a > b):
        return a
    else:
        return b


def get_max_without_arguments():
    """
        raise TypeError exception with message
    """
    raise TypeError('no arguments')


def get_max_with_one_argument(a):
    """
        return that value
    """
    return a


def get_max_with_many_arguments(*args):
    """
        return biggest number among args
    """
    r = float('-inf')
    for arg in args:
        if (arg > r):
            r = arg
    return r


def get_max_with_one_or_more_arguments(first, *args):
    """
        return biggest number among first + args
    """
    r = first
    for arg in args:
        if (arg > r):
            r = arg
    return r


def get_max_bounded(*args, low, high):
    """
        return biggest number among args bounded by low & high
    """
    r = float('-inf')
    for arg in args:
        if (arg > r) and (low < arg < high):
            r = arg
    return r


def make_max(*, low, high):
    """
        return inner function object which takes at last one argument
        and returns biggest number among it's arguments, but if the
        biggest number is bigger than the 'high' which given as required
        argument the inner function has to return it.
    """

    def inner(first, *args):
        r = float('-inf')
        for arg in (first, ) + args:
            if (arg > r) and (low < arg < high):
                r = arg
        return r

    return inner
