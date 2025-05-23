from utils.test_utils import mixer, reverse, status, APITestCase
from books.models import Book, Author
from utils import UserTypeChoices

class RetrieveBooksTestCase(APITestCase):

    def setUp(self):
        self.user = mixer.blend('users.user')
        self.author = mixer.blend(Author)
        self.book = mixer.blend(Book, author=self.author)
        self.url = reverse('books:retrieve_book', kwargs={'id' : self.book.id})

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

    def test_wrong_book_id(self):
        self.client.force_authenticate(self.user)
        url = reverse('books:retrieve_book', kwargs={'id' : self.book.id + 1})

        response = self.client.get(url)

        data = {'detail': 'Not found.'}

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertDictEqual(data, response.json())

    def test_correct_book_id(self):
        self.client.force_authenticate(self.user)

        response = self.client.get(self.url)

        data = {
                "id": self.book.id,
                "author": {
                    "id": self.author.id,
                    "author_name": self.author.author_name,
                    "birth_date": self.author.birth_date.strftime('%Y-%m-%d'),
                    "picture": f"http://testserver{self.author.picture.url}",
                    "description": self.author.description
                },
                "title": self.book.title,
                "cover": f"http://testserver{self.book.cover.url}",
                "description": self.book.description,
                "publish_year": self.book.publish_year
            }

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertDictEqual(data, response.json())