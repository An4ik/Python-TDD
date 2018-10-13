

def get_min(a, b):
    """
        return minimum among a and b
    """
    if a>b:
        return b
    else:
        return a


def get_min_without_arguments():
    """
        raise TypeError exception with message
    """
    raise TypeError('Something is happened')


def get_min_with_one_argument(x):
    """
        return that value
    """
    return x

def get_min_with_many_arguments(*args):
    """
        return smallest number among args
    """
    u = args[0]
    for i in args:
        if i<u:
            u = i
    return u

def get_min_with_one_or_more_arguments(first, *args):
    """
        return smallest number among first + args
    """
    u = first
    for i in args:
        if i<u:
            u = i
    return u


def get_min_bounded(*args, low, high):
    """
        return smallest number among args bounded by low & high
    """
    u = high
    for i in args:
        if i<u and low<i<high :
            u = i
    return u


def make_min(*, low, high):
    """
        return inner function object which takes at last one argument
        and return smallest number amount it's arguments, but if the
        smallest number is lower than the 'low' which given as required
        argument the inner function has to return it.
    """

    def inner(first, *args):
        u = high
        for i in args:
            if i<u and low<i<high:
                u = i
        return u

    return inner

