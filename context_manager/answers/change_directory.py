import os
from contextlib import contextmanager


def change_dir_without_context_manager(filename1, filename2):
    cwd = os.getcwd()
    os.chdir(filename1)
    a = os.listdir()
    os.chdir(cwd)

    cwd = os.getcwd()
    os.chdir(filename2)
    b = os.listdir()
    os.chdir(cwd)
    return a + b


@contextmanager
def change_dir(filename):
    try:
        cwd = os.getcwd()
        os.chdir(filename)
        yield
    finally:
        os.chdir(cwd)


def try_change_dir(filename):
    with change_dir(filename):
        return os.listdir()
