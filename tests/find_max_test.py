from unittest import TestCase 
import find_max as f

class FindMaxTest(TestCase):
    def test_get_max(self):
        result = f.get_max(2, 40)
        self.assertEqual(result, 40)

    def test_get_max_without_arguments(self):
        self.assertRaises(TypeError, f.get_max_without_arguments)

    def test_get_max_with_one_argument(self):
        result = f.get_max_with_one_argument(40)
        self.assertEqual(result,40);

    def test_get_max_with_many_arguments(self):
        result = f.get_max_with_many_arguments(10, 20, 30, 40)
        self.assertEqual(40, result)

    def test_get_max_with_one_or_more_arguments(self):
        first = 124
        array = [1123, 1421, 12]
        result = f.get_max_with_one_or_more_arguments(first, *array)
        self.assertEqual(1123, result)

    def test_get_max_bounded(self):
        kwargs = {
            'low': 1,
            'high': 100
        }
        result = f.get_max_bounded(-54, 45, 23, **kwargs)
        self.assertEqual(45, result)

    def test_make_max(self):
        bounded_max = f.make_max(low=0, high=255)
        self.assertEqual(True, callable(bounded_max))

        if callable(bounded_max):
            result = bounded_max(-5, 12, 13)
            self.assertEqual(13, result)
