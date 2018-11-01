"""
Fibanacci implementation using dynamic programming.
"""


class Fibonacci:

    def __init__(self):
        """
        Attributes:
            - numbers - list storing fibonacci numbers by index (n-th index stores n-th number).
        """
        self.numbers = [0, 1]

    def get_number(self, n):
        """
        Returns n-th number of fibonacci numbers.

        Iterates through the range(2, n + 1) and dynamically find i-th number by storing previous numbers
        in self.numbers. By this way we avoid recalculating previous numbers.

        :param n: n-th number of fibonacci numbers

        :return: fibonacci number
        :rtype: int
        """
        if n < 0:
            raise TypeError('Please, enter positive number.')

        for i in range(2, n + 1):
            current_fib_number = self.numbers[i - 1] + self.numbers[i - 2]
            self.numbers.append(current_fib_number)

        return self.numbers[n]
