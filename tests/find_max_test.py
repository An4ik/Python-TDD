from unittest import TestCase

import find_max as f

class FindMaxTest(TestCase):
    def test_get_max(self):
        res = f.get_max(1, 7)
        self.assertEqual(res, 7)

    def test_get_max_without_arguments(self):
        self.assertRaises(TypeError, f.get_max_without_arguments)

    def test_get_max_with_one_argument(self):
        res = f.get_max_with_one_argument(2)
        self.assertEqual(res, 2)

    def test_get_max_with_many_arguments(self):
        res = f.get_max_with_many_arguments(2, 3, 5)
        self.assertEqual(res, 5)

    def test_get_max_with_one_or_more_arguments(self):
        res = f.get_max_with_one_or_more_arguments(8, 13, 21)
        self.assertEqual(res, 21)

    def test_get_max_bounded(self):
        kwards = {
            'low': 21,
            'high': 34
        }
        res = f.get_max_bounded(2, 3, 44, 23, **kwards)
        self.assertEqual(res, 23)

    def test_make_max(self):
        bounded_max = f.make_max(low=0, high=255)
        self.assertEqual(True, callable(bounded_max))
        
        if callable(bounded_max):
            result = bounded_max(-5, 12, 13)
            self.assertEqual(13, result)
