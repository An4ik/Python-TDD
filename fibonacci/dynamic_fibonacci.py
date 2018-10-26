"""
Fibonacci number.
Fibonacci number a series of numbers in which each number ( Fibonacci number ) is the sum of the two previous numbers.
The simplest is the series 1, 1, 2, 3, 5, 8, etc.
"""


class DynamicFibonacci(object):
    """
    In this DynamicFibonacci class, we realized dynamic implementation.
    """

    def __init__(self):
        """
        __init__ method can be called as constructor on other languages. Interpretator called when you create an
        instance.

        Here you need initialize some dictionary variable which will be store values of fibonacci.
        """
        pass

    def dynamic_implementation(self, n):
        """
        :param n: n-th number of fibonacci numbers
        :rtype: int
        :return: fibonacci number

        Dynamic programming is a way to solve complex problems, breaking them down into simpler subtasks.

        You must determine the number n is negative or positive. If the number is negative, then you need to raise the error.
        After that you need to create two initial variables which is equal to 0 and 1 or you can use dictionary created above.
        Now you need for one iteration to calculate the Fibonacci number using this formula [(i - 1) + (i - 2)] using previously created variables.
        """
        pass

    