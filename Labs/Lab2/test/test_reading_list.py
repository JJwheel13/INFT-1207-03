import unittest
from Lab2.src.reading_list import add_book, list_books, search_book, delete_book


class TestReadingList(unittest.TestCase):
    def test_add_book_complete(self):
        # Assert if a book returns successfully.
        self.assertTrue(add_book("Test Book", "Author Name", "2022"))

    def test_add_book_blank_title(self):
        # Assert if a blank title returns with an error.
        self.assertFalse(add_book("", "Author Name", "2023"))

    def test_add_book_blank_author(self):
        # Assert if a blank author returns with an error.
        self.assertFalse(add_book("Test Book", "", "2024"))

    def  test_add_book_negative_year(self):
        # Assert if a negative date returns with an error.
        self.assertFalse(add_book("Test Book", "Author Name", "-2025"))

    def test_add_book_invalid_year(self):
        # Assert if an invalid date returns with an error.
        self.assertFalse(add_book("Test Book", "Author Name", "TwentyTwentySix"))

    def test_list_books_complete(self):
        # Assert if a list of valid books returns successfully.
        self.assertTrue(list_books())

    def test_search_book_complete(self):
        # Assert if searching for a known book returns successfully.
        add_book("Searched Book", "Author Name", "2027")
        self.assertTrue(search_book("Searched Book"))

    def test_search_book_invalid(self):
        # Assert if searching for an unknown book returns with an error.
        self.assertFalse(search_book("ThisBookDoesn'tExist"))

    def test_delete_book_complete(self):
        # Assert if deleting a known book returns successfully.
        add_book("Deleted Book", "Author Name", "2028")
        self.assertTrue(delete_book("Deleted Book"))

    def test_delete_book_invalid(self):
        # Assert if deleting an unknown book returns with an error.
        self.assertFalse(delete_book("ThisBookDoesn'tExistEither"))

if __name__ == '__main__':
    unittest.main()