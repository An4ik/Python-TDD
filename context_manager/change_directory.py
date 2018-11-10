import os
from contextlib import contextmanager


def change_dir_without_context_manager(filename1, filename2):
   """
   Changes directory from pwd to pwd/filename.
   :param filename1: name of first folder
   :param filename2: name of second folder
   :return: list if files in filename1 and filename2
   """


"""
With context manager.
"""


@contextmanager
def change_dir(filename):
   """
   Changes directory from pwd to pwd/filename.
   :param filename: name of folder
   """


def try_change_dir(filename):
    """
    Uses change_dir().
    :param filename: name of folder
    :return: list of files in folder
    """

