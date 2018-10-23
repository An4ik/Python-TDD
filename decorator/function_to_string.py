
def stringify(function):
    def wrapper(*args):
        return str(function(*args))
    return wrapper

   
@stringify
def add_numbers(first_number, second_number):
	return first_number + second_number

@stringify
def multiply_numbers(first_number, second_number):
    return first_number * second_number
