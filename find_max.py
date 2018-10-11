def get_max(a, b):
    """
        return max number among a and b
    """
    return a if a > b else b


def get_max_without_arguments():
    """
        raise TypeError exception with message
    """
    raise TypeError("No arguments.")


def get_max_with_one_argument(a):
    """
        return that value
    """
    return a


def get_max_with_many_arguments(*args):
    """
        return biggest number among args
    """
    maxx = -float('inf')
    for i in args:
        maxx = i if (i > maxx) else maxx
    return maxx


def get_max_with_one_or_more_arguments(first, *args):
    """
        return biggest number among first + args
    """
    return first if first > get_max_with_many_arguments(*args) else get_max_with_many_arguments(*args)


def get_max_bounded(*args, low, high):
    """
        return biggest number among args bounded by low & high
    """
    maxx = -float('inf')
    for i in args:
        if i >= low and i <= high:
            maxx = i if i > maxx else maxx;
    return maxx


def make_max(*, low, high):
    """
        return inner function object which takes at last one argument
        and return biggest number amount it's arguments, but if the
        biggest number is lower than the 'low' which given as required
        argument the inner function has to return it.
    """
    def inner(first, *args):
        return get_max_bounded(first, *args, low = low, high = high)
    return inner
