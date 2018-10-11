def get_min(a, b):
    """
        return min number among a and b
    """
    return a if a < b else b


def get_min_without_arguments():
    """
        raise TypeError exception with message
    """
    raise TypeError('missed arguments')


def get_min_with_one_argument(x):
    """
        return that value
    """
    return x


def get_min_with_many_arguments(*args):
    """
        return smallest number among args
    """
    result = float('inf')
    for arg in args:
        if arg < result:
            result = arg
    return result


def get_min_with_one_or_more_arguments(first, *args):
    """
        return smallest number among first + args
    """
    result = float('inf')
    for arg in (first,) + args:
        if arg < result:
            result = arg
    return result


def get_min_bounded(*args, low, high):
    """
        return smallest number among args bounded by low & high
    """
    res = float('inf')
    for arg in args:
        if arg < res and low < arg < high:
            res = arg
    return res


def make_min(*, low, high):
    """
        return inner function object which takes at last one argument
        and return smallest number amount it's arguments, but if the
        smallest number is lower than the 'low' which given as required
        argument the inner function has to return it.
    """

    def inner(first, *args):
        result = float('inf')

        for arg in (first,) + args:
            if arg < result and low < arg < high:
                result = arg
        return result

    return inner
