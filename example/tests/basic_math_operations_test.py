"""
You can also write some instructions here.
"""

from unittest import TestCase

from example.basic_math_operations import Number


class NumberTestCase(TestCase):
    """
    You can also write some instructions here.
    """

    def test_init(self):
        """
        It should be possible to create the Number object with one positional argument which is the value.
        """
        number = Number(10)
        self.assertIsNone(number)

    def test_init_without_argument(self):
        """
        The error should have the TypeError and message is "You can't create Number object without argument."
        """

    def test_init_with_float(self):
        number = Number(12.2)
        self.assertEqual(number, 12)

    def test_init_with_string(self):
        """
        ......
        """

    def test_init_with_double(self):
        """
        ......
        """

    def test_add(self):
        """
        It should be possible to use add operator for two objects of Number.
        """
        result = Number(4) + Number(3)
        self.assertEqual(result, 7)

    def test_subtract(self):
        """
        It should be possible to use subtract operator for two objects of Number.
        """
        result = Number(4) - Number(3)
        self.assertEqual(result, 1)

    def test_multiply(self):
        """
        ......
        """
