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
    if func is None:
        return partial(print_result_with_prefix, prefix=prefix)
    def inner(*args, **kwargs):
        """ 
        Return prefix added to result of function.
        :return: string
        """
        result = func(*args, **kwargs)
        return prefix+str(result)
    return inner

@print_result_with_prefix(prefix='The return value is ')
"""
Call decorator with named argument 'prefix'
"""
def add_numbers_with_prefix(first_number, second_number):
    """ 
    Return addition of two numbers.
    :param first_number, second_number: two integers, consecutively. 
    :return: int
    """
    return first_number + second_number

