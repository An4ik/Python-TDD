"""
Fibanacci implementation using dynamic programming.
"""


class DynamicFibonacci:
    """
    """

    def __init__(self):
        """
        Attributes:
            - cache - key/value pairs storing element number as a key and it's value as fib number.
        """
        self.cache = {}

    def get_number(self, n):
        """
        :param n: n-th number of fibonacci numbers

        :return: fibonacci number
        :rtype: int


        """
        if n < 0:
            raise TypeError('please enter positive numbers')

        self.cache[0] = 0
        if n > 0:
            self.cache[1] = 1
            for i in range(2, n + 1):
                self.cache[i] = self.cache[i - 1] + self.cache[i - 2]

        return self.cache[n]
