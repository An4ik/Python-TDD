from unittest import TestCase

from decorator.stringify import add, multiply


class StringifyTestCase(TestCase):
    def test_add_returns_string(self):
        result = add(5, 6)
        self.assertTrue(isinstance(result, str))

    def test_add_does_right_calculation(self):
        result = add(5, 6)
        self.assertEqual(int(result), 11)

    def test_multiply_returns_string(self):
        result = multiply(5, 6)
        self.assertTrue(isinstance(result, str))

    def test_multiply_does_right_calculation(self):
        result = multiply(5, 6)
        self.assertEqual(int(result), 30)
