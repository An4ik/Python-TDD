
def get_min(a, b):
    """
        return min number among a and b
    """
    if a<b: return a
    else: return b

def get_min_without_arguments():
    """
        raise TypeError exception with message
        The raise statement allows the programmer to force a specified exception to occur
    """
    raise TypeError('Error cause no arguments')
def get_min_with_one_argument(x):
    """
        return that value
    """
    return x

def get_min_with_many_arguments(*args):
    """
        return smallest number among args
    """
    result = args[0]
    for num in args:
        if(num<result):
            result = num
    return result
def get_min_with_one_or_more_arguments(first, *args):
    """
        return smallest number among first + args
    """
    result = first
    for num in args:
        if(num<result):
            result = num
    return result
def get_min_bounded(*args, low, high):
    """
        return smallest number among args bounded by low & high
    """
    result = args[0]
    for num in args:
        if(result<=low or result>=high):
            result = num
        if (num>low and num<high and num<result):
            result= num
    if(result>low and result<high):
        return result
    else:
        return None
def make_min(*, low, high):
    """
        return inner function object which takes at last one argument
        and return smallest number amount it's arguments, but if the
        smallest number is lower than the 'low' which given as required
        argument the inner function has to return it.
    """
    def inner(first, *args):
        result = first
        for num in args:
            if (result <= low or result >= high):
                result = num
            if (num > low and num < high and num<result):
                result = num
        if (result > low and result < high):
            return result
    return inner
