from utils.test_utils import mixer, reverse, status, APITestCase
from books.models import Book, Review
from utils import UserTypeChoices

class ListReviewsTestCase(APITestCase):

    def setUp(self):
        self.user = mixer.blend('users.user')
        self.reviewer_1 = mixer.blend('users.user')
        self.book = mixer.blend(Book)
        self.review = mixer.blend(Review, book=self.book, reviewer=self.reviewer_1, rating=1)
        self.url = reverse('books:review_crud', kwargs={'book_id' : self.book.id})

    def test_not_authenticated(self):

        response = self.client.get(self.url)

        data = {'detail': 'Authentication credentials were not provided.'}

        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
        self.assertDictEqual(data, response.json())

    def test_not_customer_role(self):
        self.user.user_type = UserTypeChoices.STAFF
        self.user.save()

        self.client.force_authenticate(self.user)

        response = self.client.get(self.url)

        data = {'detail': 'You do not have permission to perform this action.'}

        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
        self.assertDictEqual(data, response.json())

    def test_wrong_book_id(self):
        self.client.force_authenticate(self.user)
        url = reverse('books:review_crud', kwargs={'book_id' : self.book.id + 1})

        response = self.client.get(url)

        self.assertEqual(0, response.json()["count"])

    def test_correct_book_id_no_filters(self):
        self.client.force_authenticate(self.user)

        response = self.client.get(self.url)

        data = [
                    {
                        "reviewer": {
                            "username": self.reviewer_1.username
                        },
                        "rating": self.review.rating,
                        "comment": self.review.comment,
                        "updated_at": self.review.updated_at.strftime('%Y-%m-%d %H:%M:%S')
                    }
                ]

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(data, response.json()["results"])

    def test_correct_book_id_rating_filter(self):
        self.client.force_authenticate(self.user)

        self.reviewer_2 = mixer.blend('users.user')
        self.review_2 = mixer.blend(Review, book=self.book, reviewer=self.reviewer_2, rating=4)

        response = self.client.get(self.url + "?rating=4")

        data = [
                    {
                        "reviewer": {
                            "username": self.reviewer_2.username
                        },
                        "rating": self.review_2.rating,
                        "comment": self.review_2.comment,
                        "updated_at": self.review_2.updated_at.strftime('%Y-%m-%d %H:%M:%S')
                    }
                ]

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(data, response.json()["results"])