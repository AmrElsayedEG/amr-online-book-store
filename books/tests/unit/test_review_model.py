from utils.test_utils import mixer, TestCase
from books.models import Book, Review

class ReviewModelTest(TestCase):

    def test_review_creation(self):
        review = mixer.blend(Review)

        self.assertIsInstance(review, Review)

        self.assertIsNotNone(review.id)

    def test_review_books_related_name(self):
        book = mixer.blend(Book)
        mixer.blend(Review, book=book)

        self.assertEqual(1, book.book_reviews.all().count())


    def test_review_reviewer_related_name(self):
        reviewer = mixer.blend('users.user')
        mixer.blend(Review, reviewer=reviewer)

        self.assertEqual(1, reviewer.user_reviews.all().count())

