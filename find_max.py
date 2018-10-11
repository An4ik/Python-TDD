def get_max(a, b):
    if(a>b):
    	return a;
    else:
    	return b;


def get_max_without_arguments():
    raise TypeError("At least 1 argument must be given");


def get_max_with_one_argument(a):
    return a


def get_max_with_many_arguments(*args):
    maximum = float('-inf')
    for arg in args:
        if arg > maximum:
            maximum = arg
    return maximum


def get_max_with_one_or_more_arguments(first, *args):
    maximum = float('-inf')
    for arg in (first,)+args:
        if arg > maximum:
            maximum = arg
    return maximum


def get_max_bounded(*args, low, high):
    maximum = float('-inf')
    for arg in args:
        if arg > maximum and low < arg < high:
            maximum = arg
    return maximum


def make_max(*, low, high):
    def inner(first, *args):
        maximum = float('-inf')

        for arg in (first,) + args:
            if arg > maximum and low < arg < high:
                maximum = arg
        return maximum

    return inner
