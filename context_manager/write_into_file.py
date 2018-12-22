from contextlib import contextmanager


def write_without_context_manager(filename):
    """
    Writes 'simple open and write done!' into filename.
    :param filename: txt file
    :return: boolean, true if file closed
    """


def write_with_context_manager(filename):
    """
    Writes 'write with context manager done!' into filename.
    :param filename: txt file
    :return: boolean, true if file closed
    """


"""
GeneratorContextManager object.
"""


@contextmanager
def open_file(file, mode):
    """
    :param file: txt file
    :param mode: w for write
    """


def check_open_file(filename):
    """
    Writes 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.' into filename using open_file().
    :param filename: txt file
    :return: boolean, true is file closed
    """


def read_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            return format(line)
