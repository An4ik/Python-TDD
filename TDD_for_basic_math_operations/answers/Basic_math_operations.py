class Number(object):
    """
    Used for basic math operations.
    """

    def __init__(self, value):
        """
        Constructor of the class, interpretator called when you create an instance

        :param value : value  of the Object.
        :param type value : int

        if value is not number then returns error
        """
        if not isinstance(value, int):
            raise TypeError("Value must be real number.")
        self.value = value

    def __add__(self, other):
        """
        Addition of two numbers
        :param other : other object of the class.

        :return Sum of two object values
        """
        return self.value + other.value

    def __sub__(self, other):
        """
        Subtraction of two numbers
        :param other : value  of the Object.
        :param type value : int
        """
        if other.value > self.value:
            raise ValueError("Second value is bigger than first value")
        return self.value - other.value

    def __mul__(self, other):
        """
        Multiplication of two numbers
        :param value : value  of the Object.
        :param type value : int
        """
        return self.value * other.value

    def __truediv__(self, other):
        """
        Division of two numbers
        :param value : value  of the Object.
        :param type value : int
        """
        if other.value == 0:
            raise ValueError("Zero division error.")
        return self.value / other.value

    def __mod__(self, other):
        """
        Mod of division
        :param value : value  of the Object.
        :param type value : int
        """
        if other.value == 0:
            raise ZeroDivisionError("Zero division error.")
        return self.value % other.value

    def __eq__(self, other):
        """
        Compares two numbers for equality
        :param value : value  of the Object.
        :param type value : boolean expression
        """
        return self.value == other.value

    def __gt__(self, other):
        """
        Greater than operator (self.value > other.value)
        :param value : value  of the Object.
        :param type value : boolean expression
        """
        return self.value > other.value

    def __lt__(self, other):
        """
        Less than operator (self.value < other.value)
        :param value : value  of the Object.
        :param type value : boolean expression
        """
        return self.value < other.value
