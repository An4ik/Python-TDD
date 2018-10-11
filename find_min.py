def get_min(a, b):
    """
        return min number among a and b
    """
    return a if a < b else b

def get_min_without_arguments():
    """
        raise TypeError exception with message
    """
    raise TypeError("No arguments.")

def get_min_with_one_argument(x):
    """
        return that value
    """
    return x

def get_min_with_many_arguments(*args):
    """
        return smallest number among args
    """
    mini = float('inf')
    for i in args:
        mini = i if (i < mini) else mini
    return mini

def get_min_with_one_or_more_arguments(first, *args):
    """
        return smallest number among first + args
    """
    return first if first < get_min_with_many_arguments(*args) else get_min_with_many_arguments(*args)

def get_min_bounded(*args, low, high):
    """
        return smallest number among args bounded by low & high
    """
    mini = float('inf')
    for i in args:
        if i >= low and i <= high:
            mini = i if i < mini else mini;
    return mini

def make_min(*, low, high):
    """
        return inner function object which takes at last one argument
        and return smallest number amount it's arguments, but if the
        smallest number is lower than the 'low' which given as required
        argument the inner function has to return it.
    """
    def inner(first, *args):
        return get_min_bounded(first, *args, low = low, high = high)
    return inner
