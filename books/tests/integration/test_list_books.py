from utils.test_utils import mixer, reverse, status, APITestCase
from books.models import Book
from utils import UserTypeChoices

class ListBooksTestCase(APITestCase):

    def setUp(self):
        self.user = mixer.blend('users.user')
        self.url = reverse('books:list_books')
        self.book_1 = mixer.blend(Book, title="book_1", publish_year=2024)
        self.book_2 = mixer.blend(Book, title="book_2", publish_year=2025)

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

    def test_method_not_allowed(self):
        self.client.force_authenticate(self.user)

        response = self.client.post(self.url)

        data = {'detail': 'Method "POST" not allowed.'}

        self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)
        self.assertDictEqual(data, response.json())

    def test_list_all_no_params(self):
        self.client.force_authenticate(self.user)

        response = self.client.get(self.url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, response.json()["count"])

    def test_list_all_filter_published_year(self):
        self.client.force_authenticate(self.user)

        response = self.client.get(self.url + "?publish_year=2024")

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, response.json()["count"])

    def test_list_all_search_title(self):
        self.client.force_authenticate(self.user)

        response = self.client.get(self.url + "?search=book_1")

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, response.json()["count"])