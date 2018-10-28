from unittest import TestCase

from basic_math_operations import Number


class BasicMathOperationsTestCase(TestCase):
    """
    Tests for all basic math operations:
     -) addition
     2) subtraction
     3) division
     4) multiplication
     5) mode of division,
    equality, greater than, less than. Test for existence of some errors: TypeError, DivisionByZero.
    """

    def test_addition(self):
        """
        That function tests  for a right answer of addition of two values. Compares with expected value.
        """
        result = Number(1) + Number(2)
        self.assertEqual(result, 3)

    def test_type_error(self):
        """
        Checks whether type of number is integer or not.
        """
        with self.assertRaises(TypeError):
            Number('first_value') + Number('second_value')

    def test_subtraction(self):
        """
        Checks whether operation is working properly by condition of subtraction function.
        """
        result = Number(3) - Number(2)
        self.assertEqual(result, 1)

    def test_subtraction_less_than_greater(self):
        """
            Function tests whether greater_than function is checking two numbers correctly.
         """
        with self.assertRaises(ValueError):
            Number(3) - Number(4)

    def test_division(self):
        """
            Checks division function is dividing numbers correctly or not.
        """
        result = Number(1) / Number(2)
        self.assertAlmostEqual(result, 0.5)

    def test_division_by_zero(self):
        """
            Checks for correctness of functions when we divide two numbers, if second value == 0 returns error.
        """
        with self.assertRaises(ValueError):
            Number(3) / Number(0)

    def test_multiplication(self):
        """
            Checks whether multiplication function multiplies two numbers correctly, without any errors.
        """
        result = Number(3) * Number(2)
        self.assertEqual(result, 6)

    def test_mod_of_division(self):
        """
            Checks whether function mod_of_division is works properly.
        """
        result = Number(3) % Number(2)
        self.assertEqual(result, 1)

    def test_mod_of_division_by_zero(self):
        """
            Checks for correctness of functions when we mod of division, if second value == 0 returns error.
        """
        with self.assertRaises(ValueError):
            Number(3) / Number(0)

    def test_equality_operator(self):
        """
            Checks whether function equality_error checks correctly the equality of two numbers.
        """
        result = Number(-2) == Number(2)
        self.assertEqual(result, False)

    def test_greater_than_operator(self):
        """
            Checks whether function greater than checks correctly the greater number among two.
        """
        result = Number(-2) > Number(2)
        self.assertEqual(result, False)

    def test_less_than_operator(self):
        """
            Checks whether function greater than checks correctly the smaller number among two.
        """
        result = Number(-2) < Number(2)
        self.assertEqual(result, True)
