

def get_min(a, b):
    """
        return min number among a and b
    """


def get_min_without_arguments():
    """
        raise TypeError exception with message
    """


def get_min_with_one_argument(x):
    """
        return that value
    """


def get_min_with_many_arguments(*args):
    """
        return smallest number among args
    """


def get_min_with_one_or_more_arguments(first, *args):
    """
        return smallest number among first + args
    """


def get_min_bounded(*args, low, high):
    """
        return smallest number among args bounded by low & high
    """


def make_min(*, low, high):
    """
        return inner function object which takes at last one argument
        and return smallest number amount it's arguments, but if the
        smallest number is lower than the 'low' which given as required
        argument the inner function has to return it.
    """

    def inner(first, *args):
        pass

    return inner