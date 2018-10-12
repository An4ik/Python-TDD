from unittest import TestCase

import find_max as f


class FindMaxTest(TestCase):
    def test_get_max(self):
        result = f.get_max(1, 34)
        self.assertEqual(result, 34)

    def test_get_max_without_arguments(self):
        self.assertRaises(TypeError, f.get_max_without_arguments)

    def test_get_max_with_one_argument(self):
        result = f.get_max_with_one_argument(123)
        self.assertEqual(result, 123)

    def test_get_max_with_many_arguments(self):
        result = f.get_max_with_many_arguments(1, 2, 3, 4)
        self.assertEqual(result, 4)

    def test_get_max_with_one_or_more_arguments(self):
        first = 124
        array = [1123, 1421, 12]
        result = f.get_max_with_one_or_more_arguments(first, *array)
        self.assertEqual(result, 1421)

    def test_get_max_bounded(self):
        kwargs = {
            'low': 0,
            'high': 127
        }
        result = f.get_max_bounded(-54, 45, 23, **kwargs)
        self.assertEqual(result, 45)

    def test_make_max(self):
        bounded_max = f.make_max(low = 0, high = 255)
        self.assertEqual(True, callable(bounded_max))

        if (callable(bounded_max)):
            result = bounded_max(-5, 12, 13)
            self.assertEqual(result, 13)
