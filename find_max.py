def get_max(a, b):
	# return max number between a and b
    if(a>b):
    	return a;
    else:
    	return b;


def get_max_without_arguments():
	# raise TypeError exception with message
    raise TypeError("At least 1 argument must be given");


def get_max_with_one_argument(a):
	# return that value
    return a


def get_max_with_many_arguments(*args):
	# return greatest number among args
    maximum = float('-inf')
    for arg in args:
        if arg > maximum:
            maximum = arg
    return maximum


def get_max_with_one_or_more_arguments(first, *args):
	# return greatest number among first + args
    maximum = float('-inf')
    for arg in (first,)+args:
        if arg > maximum:
            maximum = arg
    return maximum


def get_max_bounded(*args, low, high):
	# return greatest number among args bounded by low & high
    maximum = float('-inf')
    for arg in args:
        if arg > maximum and low < arg < high:
            maximum = arg
    return maximum


def make_max(*, low, high):
	# return inner function object which takes at last one argument
    # and return greatest number amount it's arguments, but if the
    # greatest number is greater than the 'high' which given as required
    # argument the inner function has to return it.

    def inner(first, *args):
        maximum = float('-inf')

        for arg in (first,) + args:
            if arg > maximum and low < arg < high:
                maximum = arg
        return maximum

    return inner
