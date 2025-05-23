from utils.test_utils import mixer, reverse, status, APITestCase
from books.models import Book, Review
from utils import UserTypeChoices

class CUDReviewsTestCase(APITestCase):

    def setUp(self):
        self.user = mixer.blend('users.user')
        self.book = mixer.blend(Book)
        self.url = reverse('books:review_crud', kwargs={'book_id' : self.book.id})

    def test_not_authenticated(self):

        response = self.client.post(self.url)

        data = {'detail': 'Authentication credentials were not provided.'}

        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
        self.assertDictEqual(data, response.json())

    def test_not_customer_role(self):
        self.user.user_type = UserTypeChoices.STAFF
        self.user.save()

        self.client.force_authenticate(self.user)

        response = self.client.post(self.url)

        data = {'detail': 'You do not have permission to perform this action.'}

        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
        self.assertDictEqual(data, response.json())

    def test_wrong_book_id(self):
        self.client.force_authenticate(self.user)
        url = reverse('books:review_crud', kwargs={'book_id' : self.book.id + 1})

        data = {
            "rating" : 4,
            "comment" : "Good Book!"
        }

        response = self.client.post(url, data)

        data = {'detail': 'Not found.'}

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertDictEqual(data, response.json())

    def test_missing_rating(self):
        self.client.force_authenticate(self.user)

        data = {
            "comment" : "Good Book!"
        }

        response = self.client.post(self.url, data)

        data = {'rating': ['This field is required.']}

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertDictEqual(data, response.json())

    def test_wrong_rating_value(self):
        self.client.force_authenticate(self.user)

        data = {
            "rating" : 6,
            "comment" : "Good Book!"
        }

        response = self.client.post(self.url, data)

        data = {'rating': ['Ensure this value is less than or equal to 5.']}

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertDictEqual(data, response.json())

    def test_create_review_success(self):
        self.client.force_authenticate(self.user)

        data = {
            "rating" : 3,
            "comment" : "Good Book!"
        }

        response = self.client.post(self.url, data)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertDictEqual(data, response.json())

    def test_duplicate_review(self):
        mixer.blend(Review, book=self.book, reviewer=self.user, rating=1)
        self.client.force_authenticate(self.user)

        data = {
            "rating" : 3,
            "comment" : "Good Book!"
        }

        response = self.client.post(self.url, data)

        data = {"error" : ["You already submitted a rating to this book"]}

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertDictEqual(data, response.json())

    def test_delete_review(self):
        mixer.blend(Review, book=self.book, reviewer=self.user, rating=1)
        self.client.force_authenticate(self.user)

        response = self.client.delete(self.url)

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_delete_non_existing_review(self):
        self.client.force_authenticate(self.user)

        response = self.client.delete(self.url)
        
        data = {"detail": "Review not found."}

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertDictEqual(data, response.json())

    def test_update_review(self):
        review = mixer.blend(Review, book=self.book, reviewer=self.user, rating=1)
        self.client.force_authenticate(self.user)

        data = {"rating": 3, "comment": "Nice Book"}

        response = self.client.put(self.url, data)
        
        review.refresh_from_db()

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(3, review.rating)

    def test_update_non_existing_review(self):
        self.client.force_authenticate(self.user)

        data = {"rating": 3, "comment": "Nice Book"}

        response = self.client.put(self.url, data)
        
        data = {"detail": "Review not found."}

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertDictEqual(data, response.json())