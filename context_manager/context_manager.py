"""
Imports.
"""


def simple_open_and_write_without_context_manager(filename):
    """
    Writes 'simple open and write done!' into first.txt.
    """
    if(f.closed):
        return True
    return False

    
def simple_open_and_write_with_context_manager(filename):
    """
	  Writes 'write with context manager done!' into second.txt.
    """
    if(f.closed):
        return True
    return False
        
@contextmanager
def open_file(file, mode):
    """
  	More complicated version of context manager.
	  open_file() replaces open() that was used before.
    """
        
def check_open_file(filename):
    """
    Writes 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.' into third.txt with open_file().
    """
    if(f.closed):
        return True
    return False
        


def change_dir_without_context_manager(filename1, filename2):
    """
    Gives list1 the list of files in file_one.
    Gives list2 the list of files in file_two.
    Uses os, getcwd, chdir
    """
    return list1 + list2


        
        
@contextmanager
def change_dir(filename):
    """
    Context manager that switches between directries with try, Finally, yield.
    """

def try_change_dir(filename):
    """
  	Returns list of files in filename using change_dir.
    """

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
