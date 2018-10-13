def get_max(a, b):
    """
        return maximum among a and b
    """
    if a<b:
        return b
    else:
        return a


def get_max_without_arguments():
    """
        raise TypeError exception with message
    """
    raise TypeError('Something is happened')


def get_max_with_one_argument(a):
    """
        return that value
    """
    return a


def get_max_with_many_arguments(*args):
    """
        return biggest number among args
    """
    u = args[0]
    for i in args:
        if i>u:
            u = i
    return u


def get_max_with_one_or_more_arguments(first, *args):
    """
        return biggest number among first + args
    """
    u = first
    for i in args:
        if i>u:
            u = i
    return u



def get_max_bounded(*args, low, high):
    """
        return biggest number among args bounded by low & high
    """
    u = high
    for i in args:
        if i>u and low<i<high :
            u = i
    return u


def make_max(*, low, high):
    """
        return inner function object which takes at last one argument
        and return biggest number amount it's arguments, but if the
        biggest number is bigger than the 'high' which given as required
        argument the inner function has to return it.
    """
    def inner(first, *args):
        u = high
        for i in (first,) + args:
            if i>u and low<i<high:
                u = i
        return u
    
    return inner
