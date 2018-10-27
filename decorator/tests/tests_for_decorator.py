from unittest import TestCase
import stringify_decorator as f
import decorator_with_argument as f2

class DecorateTestCase(TestCase):
    def test_add_numbers(self):
        added_numbers = f.add_numbers
        self.assertEqual(added_numbers(5,6), "11")
        self.assertEqual(added_numbers(2,7), "9")


    def test_mult_numbers(self):
        multiplicated_numbers = f.multiply_numbers
        self.assertEqual(multiplicated_numbers(5, 5), "25")
   
    def test_add_numbers_with_argument(self):
        adding_numbers_with_prefix = f2.add_numbers_with_prefix
        self.assertEqual(adding_numbers_with_prefix(5,5), "The return value is 10")
    

   