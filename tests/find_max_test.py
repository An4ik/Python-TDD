from unittest import TestCase

import find_max as f


class FunctionsTest(TestCase):
    def test_get_max(self):
        a, b = 33, 77
        result = f.get_max(a, b)
        self.assertEqual(b, result)

    def test_get_max_without_arguments(self):
        pass

    def test_get_max_with_one_argument(self):
        pass

    def test_get_max_with_many_arguments(self):
        pass

    def test_get_max_with_one_or_more_arguments(self):
        pass

    def test_get_max_bounded(self):
        pass

    def test_make_max(self):
        pass
