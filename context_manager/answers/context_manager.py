import os
from contextlib import contextmanager

def simple_open_and_write_without_context_manager(filename):
    f = open(filename ,'w')
    f.write('simple open and write done!')
    f.close()
    if(f.closed):
        return True
    else:
        return False

def simple_open_and_write_with_context_manager(filename):
    with open(filename, 'w') as f:
        f.write('write with context manager done!')
    if(f.closed):
        return True
    else:
        return False
        
#### Using contextlib ####
@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    yield f
    f.close()
        
def check_open_file(filename):
    with open_file(filename, 'w') as f:
        f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
    if(f.closed):
        return True
    else:
        return False
        
#### CD Example ####
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

def read_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            return format(line)
            
simple_open_and_write_without_context_manager('first.txt')
simple_open_and_write_with_context_manager('second.txt')
check_open_file('third.txt')
print(change_dir_without_context_manager('file_one','file_two'))
print(change_dir_without_context_manager('file_one','file_one'))
print(change_dir_without_context_manager('file_two','file_two'))
print(try_change_dir('file_one'))
print(try_change_dir('file_two'))
read_file('first.txt')
read_file('second.txt')
read_file('third.txt')
