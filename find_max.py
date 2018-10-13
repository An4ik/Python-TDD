
def get_max(a, b):
    """
        return max number among a and b
    """
    if a > b: return a
    else: return b


def get_max_without_arguments():
    """
        raise TypeError exception with message 'missed arguments'
    """
    raise TypeError("missed arguments")

def get_max_with_one_argument(a):
    """
        return max value
    """
    return a

def get_max_with_many_arguments(*args):

    """
        return maximum number among args
    """
    result = float('-inf')
    for arg in args:
        if arg > result:
            result = arg
    return result

def get_max_with_one_or_more_arguments(first, *args):
    """
        return maximum number among first + args
    """
    result = float('-inf')
    for arg in (first,) + args:
        if arg > result:
            result = arg
    return result


def get_max_bounded(*args, low, high):
    """
        return maximum number among args bounded by low & high
    """
    result = float('-inf')
    for arg in args:
        if arg > result and low < arg < high:
            result = arg
    return result


def make_max(*, low, high):
    """
        return inner function object which takes at last one argument
        and return highest number amount it's arguments, but if the
        highest number is higher than the 'high' which given as required
        argument the inner function has to return it.
    """
    
    def inner(first, *args):
        result = float('-inf')
        
        for arg in (first,) + args:
            if arg > result and low < arg < high:
                result = arg
        return result
    
    return inner
