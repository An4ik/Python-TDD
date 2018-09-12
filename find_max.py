
def get_max(a, b):
    return a if a > b else b


def get_max_without_arguments():
    pass


def get_max_with_one_argument(a):
    pass


def get_max_with_many_arguments(*args):
    pass


def get_max_with_one_or_more_arguments(first, *args):
    pass


def get_max_bounded(*args, low, high):
    pass


def make_max(*, low, high):
    def inner(first, *args):
        pass

    return inner