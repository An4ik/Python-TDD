"""
Fibanacci implementation using dynamic programming.
"""


class Fibonacci:

    def __init__(self):
        """
        Attributes:
            - numbers - list storing fibonacci numbers by index (n-th index stores n-th number).
        """

    def get_number(self, n):
        """
        Returns n-th number of fibonacci numbers.

        Iterates through the range(2, n + 1) and dynamically find i-th number by storing previous numbers
        in self.numbers. By this way we avoid recalculating previous numbers.

        :param n: n-th number of fibonacci numbers

        :return: fibonacci number
        :rtype: int
        """
