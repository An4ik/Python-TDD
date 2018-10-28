from unittest import TestCase

from fibonacci.brute_force import Fibonacci


class FibonacciTest(TestCase):

    def test_with_one_argument(self):
        """
        It should be possible to compute the Fibonacci number with one argument which is the value.
        """
        fib = Fibonacci()
        result = fib.get_number(1)
        self.assertEqual(result, 0)

    def test_with_zero_argument(self):
        """
        It should be possible to compute the Fibonacci number with value 0.
        """
        fib = Fibonacci()
        result = fib.get_number(0)
        self.assertEqual(result, 0)

    def test_with_long_argument(self):
        fib = Fibonacci()
        result = fib.get_number(343)
        self.assertEqual(result, 215414832505658809004682396169711233230800418578767753330908886771798637)

    def test_with_negative_number(self):
        fib = Fibonacci()
        with self.assertRaises(TypeError):
            fib.get_number(-14234)

    def test_with_string_argument(self):
        fib = Fibonacci()
        with self.assertRaises(TypeError):
            fib.get_number('aasd')

    def test_with_list_argument(self):
        fib = Fibonacci()
        with self.assertRaises(TypeError):
            fib.get_number([1, 2])

    def test_with_dictionary_argument(self):
        fib = Fibonacci()
        with self.assertRaises(TypeError):
            fib.get_number({1: 'fyahiduf'})

    def test_with_tuple_argument(self):
        fib = Fibonacci()
        with self.assertRaises(TypeError):
            fib.get_number((23, 123, 123))

    def test_with_many_arguments(self):
        fib = Fibonacci()
        with self.assertRaises(TypeError):
            fib.get_number(1, 2)

    def test_without_arguments(self):
        fib = Fibonacci()
        with self.assertRaises(TypeError):
            fib.get_number()
