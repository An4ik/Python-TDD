class File(object):
    """
    Context manager class with '__init__', '__enter__', '__exit__' methods that opens and closes file.
    """

def check(filename):
    """
    Writes 'Yeah! You can write context manager as class)') into filename with File class.
    :param filename: txt file
    """


def read_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            return format(line)