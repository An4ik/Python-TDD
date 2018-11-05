from unittest import TestCase

from fibonacci.brute_force import Fibonacci


class FibonacciTestCase(TestCase):

    def setUp(self):
        """
        Called for every test function.
        Actually it's we should have here common things.
        """

        self.fib = Fibonacci()

    def test_the_first_number(self):
        """
        The first number of the fibonacci numbers is 0.
        """
        result = self.fib.get_number(1)
        self.assertEqual(result, 0, 'The first number is 0, not %s' % result)

    def test_the_second_number(self):
        """
        The first number of the fibonacci numbers is 1.
        """
        result = self.fib.get_number(2)
        self.assertEqual(result, 1, 'The second number is 1, not %s' % result)

    def test_the_third_number(self):
        """
        The third number of the fibonacci numbers is 1.
        """
        result = self.fib.get_number(3)
        self.assertEqual(result, 1, 'The third number is 1, not %s' % result)

    def test_with_long_argument(self):
        result = self.fib.get_number(33)
        self.assertEqual(result, 2178309)

    def test_with_negative_number(self):
        with self.assertRaises(TypeError):
            self.fib.get_number(-10)
