"""
Fibanacci implementation using recursive method.
"""


class Fibonacci:

    def get_number(self, n):
        """
        Returns n-th number of fibonacci numbers.

        Returns 1 or 0 for 'n' less than 3, otherwise recursively calls itself with appropriate arguments
        (sum of two previous numbers).

        :param n: n-th number of fibonacci numbers
        :rtype: int
        :return: fibonacci number
        """

        if n <= 2:
            return 1 if n == 2 else 0

        return self.get_number(n - 2) + self.get_number(n - 1)
