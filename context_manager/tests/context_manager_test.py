from unittest import TestCase
import os
import cm as f

class ContextManagerTest(TestCase):
    def test_simple_without(self):
        result = f.simple_open_and_write_without_context_manager('first.txt')
        self.assertEqual(result, True)

    def test_simple_with(self):
        result = f.simple_open_and_write_with_context_manager('second.txt')
        self.assertEqual(result, True)

    def test_check_open_file(self):
        result = f.check_open_file('third.txt')
        self.assertEqual(result, True)

    def test_simple_without1(self):
        result = f.read_file('first.txt')
        self.assertEqual(result, 'simple open and write done!')

    def test_simple_with1(self):
        result = f.read_file('second.txt')
        self.assertEqual(result, 'write with context manager done!')

    def test_check_open_file1(self):
        result = f.read_file('third.txt')
        self.assertEqual(result, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

    def test_change_dir_without(self):
        result = f.change_dir_without_context_manager('file_one','file_two')
        self.assertEqual(result, ['love.txt', 'context.txt', 'I.txt', 'manager.txt', 'love.txt', 'and.txt', 'I.txt', 'beshbarmak.txt'])

    def test_change_dir_without1(self):
        result = f.change_dir_without_context_manager('file_one', 'file_one')
        self.assertEqual(result, ['love.txt', 'context.txt', 'I.txt', 'manager.txt', 'love.txt', 'context.txt', 'I.txt', 'manager.txt'])

    def test_change_dir_without2(self):
        result = f.change_dir_without_context_manager('file_two', 'file_two')
        self.assertEqual(result, ['love.txt', 'and.txt', 'I.txt', 'beshbarmak.txt', 'love.txt', 'and.txt', 'I.txt', 'beshbarmak.txt'])


    def test_change_dir_with(self):
        result = f.try_change_dir('file_one')
        self.assertEqual(result, ['love.txt', 'context.txt', 'I.txt', 'manager.txt'])

    def test_change_dir_with1(self):
        result = f.try_change_dir('file_two')
        self.assertEqual(result,['love.txt', 'and.txt', 'I.txt', 'beshbarmak.txt'])
