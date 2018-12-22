from unittest import TestCase
from context_manager_as_class import (
    check,
    read_file
)

class LevelOneTest(TestCase):
    def test_write_with1(self):
        check('first.txt')
        result = read_file('first.txt')
        self.assertEqual(result, 'Yeah! You can write context manager as class)')