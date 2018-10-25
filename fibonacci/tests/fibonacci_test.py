from unittest import TestCase

from fibonacci import Fibonacci

class FibonacciTest(TestCase):

    def test_recursive_implementation_with_one_argument(self):
        """
        It should be possible to compute the Fibonacci number with one argument which is the value.
        """
        fib = Fibonacci()
        result = fib.recursive_implementation(34)
        self.assertEqual(result, 5702887)

    def test_dynamic_implementation_with_one_argument(self):
        """
        It should be possible to compute the Fibonacci number with one argument which is the value.
        """
        fib = Fibonacci()
        result = fib.dynamic_implementation(34)
        self.assertEqual(result, 5702887)

    def test_recursive_implementation_zero(self):
        """
        It should be possible to compute the Fibonacci number with value 0.
        """
        fib = Fibonacci()
        result = fib.recursive_implementation(0)
        self.assertEqual(result, 0)

    def test_dynamic_implementation_zero(self):
        """
        It should be possible to compute the Fibonacci number with value 0.
        """
        fib = Fibonacci()
        result = fib.dynamic_implementation(0)
        self.assertEqual(result, 0)

    def test_dynamic_implementation_with_long_argument(self):
        fib = Fibonacci()
        result = fib.dynamic_implementation(343)
        self.assertEqual(result, 215414832505658809004682396169711233230800418578767753330908886771798637)

    def test_recursive_implementation_with_long_argument(self):
        fib = Fibonacci()
        result = fib.recursive_implementation(343)
        self.assertEqual(result, 215414832505658809004682396169711233230800418578767753330908886771798637)

    def test_recursive_implementation_with_negative_number(self):
        fib = Fibonacci()
        with self.assertRaises(TypeError):
            fib.recursive_implementation(-1)

    def test_dynamic_implementation_with_negative_number(self):
        fib = Fibonacci()
        with self.assertRaises(TypeError):
            fib.dynamic_implementation(-14234)

    def test_dynamic_implementation_with_string(self):
        fib = Fibonacci()
        with self.assertRaises(TypeError):
            fib.dynamic_implementation('aasd')

    def test_recursive_implementation_with_string(self):
        fib = Fibonacci()
        with self.assertRaises(TypeError):
            fib.recursive_implementation('aasd')

    def test_recursive_implementation_with_list(self):
        fib = Fibonacci()
        with self.assertRaises(TypeError):
            fib.recursive_implementation([1, 2])

    def test_dynamic_implementation_with_list(self):
        fib = Fibonacci()
        with self.assertRaises(TypeError):
            fib.dynamic_implementation([1, 2])

    def test_recursive_implementation_with_dictionary(self):
        fib = Fibonacci()
        with self.assertRaises(TypeError):
            fib.recursive_implementation({ 1: 'Sorry' })

    def test_dynamic_implementation_with_dictionary(self):
        fib = Fibonacci()
        with self.assertRaises(TypeError):
            fib.dynamic_implementation({ 2: 'Cannot stop' })

    def test_recursive_implementation_with_tuple(self):
        fib = Fibonacci()
        with self.assertRaises(TypeError):
            fib.recursive_implementation((1, ))

    def test_dynamic_implementation_with_tuple(self):
        fib = Fibonacci()
        with self.assertRaises(TypeError):
            fib.dynamic_implementation((23, 123, 123))

    def test_dynamic_implementation_with_many_arguments(self):
        fib = Fibonacci()
        with self.assertRaises(TypeError):
            fib.dynamic_implementation(1, 2)

    def test_recursive_implementation_with_many_arguments(self):
        fib = Fibonacci()
        with self.assertRaises(TypeError):
            fib.recursive_implementation(1, 2)

    def test_recursive_implementation_without_arguments(self):
        fib = Fibonacci()
        with self.assertRaises(TypeError):
            fib.recursive_implementation()

    def test_dynamic_implementation_without_arguments(self):
        fib = Fibonacci()
        with self.assertRaises(TypeError):
            fib.dynamic_implementation()