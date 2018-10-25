#Here write your imports
import os
from contextlib import contextmanager


def simple_open_and_write_without_context_manager(filename):
    '''
        Write 'simple open and write done!' into first.txt, but take fitst.txt as argumant.
        Dont forget to close.
	3 lines
    '''
    if(f.closed):
        return True
    else:
        return False

    
def simple_open_and_write_with_context_manager(filename):
    '''
	Write 'write with context manager done!' into second.txt, but take second.txt as argument.	
	2 lines
    '''
    if(f.closed):
        return True
    else:
        return False
        
@contextmanager
def open_file(file, mode):
    '''
	Write more complicated version of context manager.
	Now open_file() must replace open() that we used before.
	Use here open(), yeild, close().
	3 lines.
    '''
        
def check_open_file(filename):
    '''
	Write 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.' into third.txt, but take third.txt as argument.	
	Use open_file().
	2 lines.
    '''
    if(f.closed):
        return True
    else:
        return False
        


def change_dir_without_context_manager(filename1, filename2):
    '''
	Give list1 the list of files in filename1.
	Give list2 the list of files in filename2.
	Use os, getcwd, chdir
    '''
    return list1 + list2


        
        
@contextmanager
def change_dir(filename):
    '''
	Here you dont need to list files, 
	couse you are writing your oun context manager that will help you to switch between directries.
	Don't forget to use try, Finally, yield.
    '''

def try_change_dir(filename):
    '''
	Return list of files in filename using change_dir that you wrote
    '''

def read_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            return format(line)
            

