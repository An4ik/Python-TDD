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
        """
        self.cache = {}

    def dynamic_implementation(self, n):
        """
        :param n: n-th number of fibonacci numbers
        :return: fibonacci number
        :rtype: int

        Dynamic programming is a way to solve complex problems, breaking them down into simpler subtasks.
        """
        if n < 0:
            raise TypeError('please enter positive numbers')

        self.cache[0] = 0
        if n > 0:
            self.cache[1] = 1
            for i in range(2, n + 1):
                self.cache[i] = self.cache[i - 1] + self.cache[i - 2]

        return self.cache[n]
