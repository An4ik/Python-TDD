from unittest import TestCase
import decorate_functions as f

class Decorate_test(TestCase):
    def test_add_numbers(self):
        added_numbers = f.add_numbers
        self.assertEqual(added_numbers(5,6), "11")
        self.assertEqual(added_numbers(2,7), "9")


    def test_mult_numbers(self):
        multiplicated_numbers = f.multiply_numbers
        self.assertEqual(multiplicated_numbers(first_number = 5, second_number = 5), "25")
   