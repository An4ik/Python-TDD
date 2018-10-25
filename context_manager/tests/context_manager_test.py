from unittest import TestCase

import cm as f

class ContextManagerTest(TestCase):
    def test_simple_without(self):
        result = f.simple_open_and_write_without_context_manager('first.txt')
        self.assertEqual(result, True)

    def test_simple_with(self):
        result = f.simple_open_and_write_with_context_manager('second.txt')
        self.assertEqual(result, True)

