from unittest import TestCase

from brute_force_fibonacci import BruteForceFibonacci

class BruteForceFibonacciTest(TestCase):

    def test_with_one_argument(self):
        """
        It should be possible to compute the Fibonacci number with one argument which is the value.
        """
        fib = BruteForceFibonacci()
        result = fib.recursive_implementation(34)
        self.assertEqual(result, 5702887)

    def test_with_zero_argument(self):
        """
        It should be possible to compute the Fibonacci number with value 0.
        """
        fib = BruteForceFibonacci()
        result = fib.recursive_implementation(0)
        self.assertEqual(result, 0)

    def test_with_long_argument(self):
        fib = BruteForceFibonacci()
        result = fib.recursive_implementation(343)
        self.assertEqual(result, 215414832505658809004682396169711233230800418578767753330908886771798637)

    def test_with_negative_number(self):
        fib = BruteForceFibonacci()
        with self.assertRaises(TypeError):
            fib.recursive_implementation(-14234)

    def test_with_string_argument(self):
        fib = BruteForceFibonacci()
        with self.assertRaises(TypeError):
            fib.recursive_implementation('aasd')

    def test_with_list_argument(self):
        fib = BruteForceFibonacci()
        with self.assertRaises(TypeError):
            fib.recursive_implementation([1, 2])

    def test_with_dictionary_argument(self):
        fib = BruteForceFibonacci()
        with self.assertRaises(TypeError):
            fib.recursive_implementation({ 1: 'fyahiduf' })

    def test_with_tuple_argument(self):
        fib = BruteForceFibonacci()
        with self.assertRaises(TypeError):
            fib.recursive_implementation((23, 123, 123))

    def test_with_many_arguments(self):
        fib = BruteForceFibonacci()
        with self.assertRaises(TypeError):
            fib.recursive_implementation(1, 2)

    def test_without_arguments(self):
        fib = BruteForceFibonacci()
        with self.assertRaises(TypeError):
            fib.recursive_implementation()