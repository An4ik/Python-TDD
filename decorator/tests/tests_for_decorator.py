from unittest import TestCase
import stringify_decorator as f
import decorator_with_argument as f2
import decorator_with_positional_argument as f3

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
    
    def test_message_print_with_argument(self):
        message = f3.hello2
        self.assertEqual(message(), "This is default message")
    
    def test_message_print_with_argument(self):
        message_with_argument = f3.hello_my_friend
        self.assertEqual(message_with_argument(), "Dear future SDU generation,\nthis is 2018! We are glad to give some piece of our knowledge to you.")

   