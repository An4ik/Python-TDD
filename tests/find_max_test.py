from unittest import TestCase
import find_max as f

class FindMaxTest(TestCase):
    def test_get_max(self):
        result = f.get_max(3,21)
        self.assertEqual(result, 21)

    def test_get_max_without_arguments(self):
        self.assertRaises(TypeError, f.get_max_without_arguments)

    def test_get_max_with_one_argument(self):
        result = f.get_max_with_one_argument(9)
        self.assertEqual(result, 9)

    def test_get_max_with_many_arguments(self):
        result = f.get_max_with_many_arguments(1, 2, 3, 4)
        self.assertEqual(4, result)

    def test_get_max_with_one_or_more_arguments(self):
        first = 9
        array = [48, 4, 12]
        result = f.get_max_with_one_or_more_arguments(first, *array)
        self.assertEqual(48, result)

    def test_get_max_bounded(self):
        kwargs = {
            'low': 0,
            'high': 34
        }
        result = f.get_max_bounded(51, 9, 20, **kwargs)
        self.assertEqual(34, result)

    def test_make_max(self):
        bounded_max = f.make_max(low=0, high=255)
        self.assertEqual(True, callable(bounded_max))
        
        if callable(bounded_max):
            result = bounded_max(-5, 12, 43)
            self.assertEqual(255, result)

