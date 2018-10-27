from functools import partial
"""
This decorator takes a prefix as an argument and adds to function's return this prefix.
"""
def print_result_with_prefix(func=None, *, prefix=''):
	""" 
	Returns the partial object of function and prefix. Hint : use as partial(func, *args, **keywords)
    :param func: any function 
	:param prefix: any string
	:return: modified function inner
	
	"""
    def inner(*args, **kwargs):
        """ 
        Return prefix added to result of function.
        :return: string
        """

"""
Call decorator with named argument 'prefix'. Hint : decorator is called with @ sign.
"""
def add_numbers_with_prefix(first_number, second_number):
    """ 
    Return addition of two numbers.
    :param first_number, second_number: two integers, consecutively. 
    :return: int
    """

