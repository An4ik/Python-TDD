from unittest import TestCase

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

    def test_change_dir_without(self):
        result = f.change_dir_without_context_manager('file_one','file_two')
        self.assertEqual(result, ['love.txt', 'context.txt', 'I.txt', 'manager.txt', 'love.txt', 'and.txt', 'I.txt', 'beshbarmak.txt'])

    def test_change_dir_without1(self):
        result = f.change_dir_without_context_manager('file_one', 'file_one')
        self.assertEqual(result, ['love.txt', 'context.txt', 'I.txt', 'manager.txt', 'love.txt', 'context.txt', 'I.txt', 'manager.txt'])

    def test_change_dir_without2(self):
        result = f.change_dir_without_context_manager('file_two', 'file_two')
        self.assertEqual(result, ['love.txt', 'and.txt', 'I.txt', 'beshbarmak.txt', 'love.txt', 'and.txt', 'I.txt', 'beshbarmak.txt'])

