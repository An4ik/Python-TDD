from contextlib import contextmanager


def write_without_context_manager(filename):
    f = open(filename, 'w')
    f.write('simple open and write done!')
    f.close()
    if (f.closed):
        return True
    return False


def write_with_context_manager(filename):
    with open(filename, 'w') as f:
        f.write('write with context manager done!')
    if (f.closed):
        return True
    return False


@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    yield f
    f.close()


def check_open_file(filename):
    with open_file(filename, 'w') as f:
        f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
    if (f.closed):
        return True
    return False


def read_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            return format(line)