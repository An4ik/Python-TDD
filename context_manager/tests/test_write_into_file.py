from unittest import TestCase
from write_into_file import (
    write_without_context_manager,
    write_with_context_manager,
    check_open_file,
    read_file
)

class LevelTwoTest(TestCase):
    def test_write_without(self):
        result = write_without_context_manager('first.txt')
        self.assertEqual(result, True)

    def test_write_with(self):
        result = write_with_context_manager('second.txt')
        self.assertEqual(result, True)

    def test_check_open_file(self):
        result = check_open_file('third.txt')
        self.assertEqual(result, True)

    def test_write_without1(self):
        result = read_file('first.txt')
        self.assertEqual(result, 'simple open and write done!')

    def test_write_with1(self):
        result = read_file('second.txt')
        self.assertEqual(result, 'write with context manager done!')

    def test_check_open_file1(self):
        result = read_file('third.txt')
        self.assertEqual(result, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.')