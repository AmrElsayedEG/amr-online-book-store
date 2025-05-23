from utils.test_utils import mixer, TestCase
from books.models import Author, Book

class AuthorModelTest(TestCase):

    def test_author_creation(self):
        author = mixer.blend(Author)

        self.assertIsInstance(author, Author)

        self.assertIsNotNone(author.id)

        self.assertEqual(author.author_name, str(author))

    def test_author_books_related_name(self):
        author = mixer.blend(Author)
        mixer.blend(Book, author=author)

        self.assertEqual(1, author.author_books.all().count())

