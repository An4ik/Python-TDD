def add_my_message(message='This is default message.'):
    """ 
    Returns message added to return value of a function to be decorated.
    :param message: any string 
    :return: modified function wrapper
    """
    def wrapper(func):
    """ 
    Contains function inner. 
    :param func: any function
    :return: modified function inner
    """
        def inner():
            """ 
            Returns message and return value of function. 
            :return: two lines of string (first line - message, second line - function's result).
            """

"""
Declare decorator with positional argument.
"""
def hello_my_friend():
    """
    Print any string.
    """
    
"""
Declare decorator without any arguments.
"""
def hello2():
    """
    Print any string.
    """
