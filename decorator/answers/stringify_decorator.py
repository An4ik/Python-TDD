def stringify(function):
	""" 
	Takes a function as an argument and changes it's return type to string.
	"""
    def inner(*args):
    	"""
    	Change return type of function given as stringify argument to string.
    	"""
        return str(function(*args))
    return wrapper


def add_numbers(first_number, second_number):
	"""
	Return the sum of two numbers.
	"""
	return first_number + second_number

def multiply_numbers(first_number, second_number):
	"""
	Return the multiplication of two numbers.
	"""
    return first_number * second_number


	