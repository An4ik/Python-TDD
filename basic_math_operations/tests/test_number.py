from unittest import TestCase

from basic_math_operations.number import Number


class NumberTestCase(TestCase):

    def test_addition(self):
        result = Number(1) + Number(2)
        self.assertEqual(result, 3)

    def test_type_error(self):

        with self.assertRaises(TypeError):
            Number('first_value') + Number('second_value')

    def test_subtraction(self):
        result = Number(3) - Number(2)
        self.assertEqual(result, 1)

    def test_subtraction_less_than_greater(self):
        with self.assertRaises(ValueError):
            Number(3) - Number(4)

    def test_division(self):
        result = Number(1) / Number(2)
        self.assertAlmostEqual(result, 0.5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            Number(3) / Number(0)

    def test_multiplication(self):
        result = Number(3) * Number(2)
        self.assertEqual(result, 6)

    def test_mod_of_division(self):
        result = Number(3) % Number(2)
        self.assertEqual(result, 1)

    def test_mod_of_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            Number(3) / Number(0)

    def test_equality_operator(self):
        result = Number(-2) == Number(2)
        self.assertEqual(result, False)

    def test_greater_than_operator(self):
        result = Number(-2) > Number(2)
        self.assertEqual(result, False)

    def test_less_than_operator(self):
        result = Number(-2) < Number(2)
        self.assertEqual(result, True)
