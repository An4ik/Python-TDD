"""
Fibonacci number.
Fibonacci number a series of numbers in which each number ( Fibonacci number ) is the sum of the two previous numbers.
The simplest is the series 1, 1, 2, 3, 5, 8, etc.
"""


class BruteForceFibonacci(object):
    """
    In this RecursiveFibonacci class, we realized recursive implementation.
    """

    def __init__(self):
        """
        __init__ method can be called as constructor on other languages. Interpretator called when you create an
        instance.

        Here you need to initialize some dictionary variable which will be store values of fibonacci.
        """
        pass

    def recursive_implementation(self, n):
        """
        :param n: n-th number of fibonacci numbers
        :rtype: int
        :return: fibonacci number

        Recursion means calling functions directly from itself.

        You must determine the number n is negative or positive. If the number is negative, then you need to raise the error.
        After that you need to check if this number is in the cache. If this number in the cache return this number.
        If not, you need to recursively find (n - 1) + (n - 2).
        Until n equals one or zero.
        """
        pass