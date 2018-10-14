"""
You can write some description here if you want.
"""


class Number(object):
    """
    Provide a number as object.

    This docs will read next generations of students. So it's your brothers and sisters. Please try do it the best.
    """

    def __init__(self, value):
        """
        __init__ method can be called as constructor on other languages. Interpretator called when you create an
        instance

        :param value: value (number) of the Object.
        """

        # describe assert here.
        assert isinstance(value, int), 'The value should have integer.'
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        if other.value < 0:
            raise TypeError('you can not sub negative.')
        return self.value - other.value
