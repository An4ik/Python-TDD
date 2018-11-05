
class Book:

    """
        A class used to represent a Book
        ...
        Attributes
        ----------
        book_name : str
            a name of employeename of book
        rating : int
            rating of book
    """

    def __init__(self, book_name, rating):
        self.book_name = book_name
        self.rating = rating

    @staticmethod
    def sort_by_name(list_of_books):
        """
        Takes list of Book objects and sorts that list by name of books

        :param list_of_books: list of Book objects
        :type list_of_books: list

        :return: sorted by name list of Book objects
        :rtype: list
        """
        pass

    @staticmethod
    def reverse_word_order_of_sentence(sentence):
        """
        Takes a sentence and reverses word order of sentence
        :param sentence: some sentence with words
        :type sentence: string

        :return: sentence with reverse word order
        :rtype: string
        """
        pass

    @staticmethod
    def concatenate_book_dicts_in_new_one(*dicts):
        """
        Takes 0 or more book dictionaries and concatenates it in new one dictionary
        :param dicts: book dictionaries, in which key is author of a book and value is name of the book
        :type dicts: tuple

        :return: concatenated dictionary that involves all elements of dictionaries which in dicts variable
        :rtype: dict
        """
        pass
