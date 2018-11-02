from unittest import TestCase

import Iterator as it


class IterTestCase(TestCase):



    def test_for_string_index(self):

        """
        Checks for string error
        """

        iterator_fisrt_index = it.Iterator("ULZ")

        self.assertRaises(TypeError, iterator_fisrt_index)



    def test_full_list_of_iterator(self):
        """
        Test checks full list of fibonacci
        """

        self.assertEqual(list(it.Iterator(4)), [0, 1, 2, 3])


    def test_check_equality_of_list_iterator(self):
        """
        Tests checks equality of the list fibonacci
        """
        self.assertListEqual(list(it.Iterator(4)), list(it.Iterator(4)))


    def test_True_for_iteration(self):
        """
        Test checks Trues of i
        """
        self.assertTrue(it.Iterator(4))

    def test_for_len_of_itterator(self):

        """
        Test checks the size of fibonacci list
        """

        self.assertEqual(len(list(it.Iterator(4))), 4)


    def test_for_checking_location(self):

        """
        Test checks location of iterator.

        iterator_list_first is the list
        iterator_list_second is the secons list

        """

        iterator_list_first = iter(it.Iterator(4))
        iterator_list_second = iter(it.Iterator(4))
        self.assertNotEqual(iterator_list_first,iterator_list_second)