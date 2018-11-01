def add_my_message(message='This is my second message.'):
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
            print(message)
            return func()
        return inner
    return wrapper

"""
Declare decorator with positional argument.
"""
@add_my_message('Dear future SDU generation,')
def hello_my_friend():
    """
    Print any string.
    """
    print ('this is 2018! We are glad to give some piece of our knowledge to you.')
"""
Declare decorator without any arguments.
"""
@add_my_message()
def hello2():
    """
    Print any string.
    """
    print ('This decorator works also without argument. Good job!')
