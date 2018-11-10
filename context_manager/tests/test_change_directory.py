from unittest import TestCase
from change_directory import (
    change_dir_without_context_manager,
    try_change_dir
)

class ContextManagerTest(TestCase):
    def test_change_dir_without(self):
        result = change_dir_without_context_manager('file_one','file_two')
        self.assertEqual(result, ['love.txt', 'context.txt', 'I.txt', 'manager.txt', 'love.txt', 'and.txt', 'I.txt', 'beshbarmak.txt'])

    def test_change_dir_without1(self):
        result = change_dir_without_context_manager('file_one', 'file_one')
        self.assertEqual(result, ['love.txt', 'context.txt', 'I.txt', 'manager.txt', 'love.txt', 'context.txt', 'I.txt', 'manager.txt'])

    def test_change_dir_without2(self):
        result = change_dir_without_context_manager('file_two', 'file_two')
        self.assertEqual(result, ['love.txt', 'and.txt', 'I.txt', 'beshbarmak.txt', 'love.txt', 'and.txt', 'I.txt', 'beshbarmak.txt'])


    def test_change_dir_with(self):
        result = try_change_dir('file_one')
        self.assertEqual(result, ['love.txt', 'context.txt', 'I.txt', 'manager.txt'])

    def test_change_dir_with1(self):
        result = try_change_dir('file_two')
        self.assertEqual(result,['love.txt', 'and.txt', 'I.txt', 'beshbarmak.txt'])