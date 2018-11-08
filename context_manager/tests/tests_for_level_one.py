from unittest import TestCase
import write_into_file as f

class LevelOneTest(TestCase):
    def test_write_without(self):
        result = f.write_without_context_manager('first.txt')
        self.assertEqual(result, True)

    def test_write_with(self):
        result = f.write_with_context_manager('second.txt')
        self.assertEqual(result, True)

    def test_check_open_file(self):
        result = f.check_open_file('third.txt')
        self.assertEqual(result, True)

    def test_write_without1(self):
        result = f.read_file('first.txt')
        self.assertEqual(result, 'simple open and write done!')

    def test_write_with1(self):
        result = f.read_file('second.txt')
        self.assertEqual(result, 'write with context manager done!')

    def test_check_open_file1(self):
        result = f.read_file('third.txt')
        self.assertEqual(result, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.')