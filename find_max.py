def get_max(a, b):
    return a if a>b else b

def get_max_without_arguments():
    raise TypeError('missed arguments')


def get_max_with_one_argument(a):
    return a


def get_max_with_many_arguments(*args):
    res = -float('inf')
    for a in args:
        if res<a:
            res = a
    return res


def get_max_with_one_or_more_arguments(first, *args):
    res = -float('inf')
    for a in (first,) + args:
        if res<a:
            res = a
    return res


def get_max_bounded(*args, low, high):
    res = -float('inf')
    for a in args:
        if res<a and low<a<high:
            res = a
    return res


def make_max(*, low, high):
    def inner(first, *args):
        res = -float('inf')
        for a in (first,)+args:
            if res<a and low<a<high:
                res = a
        return res
    
    return inner
