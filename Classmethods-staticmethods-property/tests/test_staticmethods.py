from unittest import TestCase
from staticmethods import Book


class StaticmethodsTest(TestCase):

    def test_staticmethod_sort_by_name(self):
        book_1 = Book('Fight club', 7)
        book_2 = Book('Shantaram', 8)
        book_3 = Book('Nad kukushkinim gnezdom', 7)
        list_of_books = [book_1, book_2, book_3]
        sorted_list_of_books = Book.sort_by_name(list_of_books)
        self.assertEqual(sorted_list_of_books, [book_1, book_3, book_2])

    def test_staticmethod_reverse_word_order_of_sentence(self):
        sentence = 'Lorem ipsum dolor sit amet'
        sentence_reverse_word_order = Book.reverse_word_order_of_sentence(sentence)
        self.assertEqual(sentence_reverse_word_order, 'amet sit dolor ipsum Lorem')

    def test_staticmethod_concatenate_books_dict_in_new_one(self):
        books_dict1 = {'Chuck Palahniuk': 'Fight club', 'Antoine de Saint-Exupery': 'The Little Prince'}
        books_dict2 = {'Gregory David Roberts': 'Shantaram', 'A Study in Scarlet': 'Arthur Conan Doyle'}
        books_dict3 = {'The Lord of the Rings': 'J. R. R. Tolkien'}
        concatenated_book_dict = Book.concatenate_book_dicts_in_new_one(books_dict1, books_dict2, books_dict3)
        books_dict5 = {'Chuck Palahniuk': 'Fight club', 'Antoine de Saint-Exupery': 'The Little Prince',
                       'Gregory David Roberts': 'Shantaram', 'A Study in Scarlet': 'Arthur Conan Doyle',
                       'The Lord of the Rings': 'J. R. R. Tolkien'}
        self.assertEqual(concatenated_book_dict, books_dict5)
