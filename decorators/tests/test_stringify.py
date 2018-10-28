from unittest import TestCase
from decorators.stringify import add_numbers, multiply_numbers


class StringifyTestCase(TestCase):
    def test_add_numbers_returns_string(self):
        result = add_numbers(5, 6)
        self.assertTrue(isinstance(result, str))

    def test_add_numbers_right_calculation(self):
        result = add_numbers(5, 6)
        self.assertEqual(int(result), 11)
