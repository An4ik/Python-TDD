class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()

def check(filename):
    with File(filename, 'w') as opened_file:
        opened_file.write('Yeah! You can write context manager as class)')


def read_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            return format(line)