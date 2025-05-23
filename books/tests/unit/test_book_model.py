from utils.test_utils import mixer, TestCase
from books.models import Book

class BookModelTest(TestCase):

    def test_book_creation(self):
        book = mixer.blend(Book, title='Test Book', publish_year=2025)

        self.assertIsInstance(book, Book)

        self.assertIsNotNone(book.id)

        self.assertEqual('Test Book', book.title)

        self.assertEqual(2025, book.publish_year)

        self.assertEqual("Test Book", str(book))