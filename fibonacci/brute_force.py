"""
Fibanacci implementation using recursive method.
"""


class Fibonacci(object):

    def get_number(self, n):
        """
        Returns n-th number of fibonacci numbers.

        :param n: n-th number of fibonacci numbers
        :rtype: int
        :return: fibonacci number
        """

        if n < 0:
            raise TypeError('Please, enter positive number.')

        if n <= 2:
            return 1 if n == 2 else 0

        return self.get_number(n - 2) + self.get_number(n - 1)
