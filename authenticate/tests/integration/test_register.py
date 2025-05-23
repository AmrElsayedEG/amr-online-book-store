from utils.test_utils import mixer, reverse, status, APITestCase

class RegisterTestCase(APITestCase):

    def setUp(self):
        self.url = reverse('authenticate:register')

    def test_method_not_allowed(self):

        response = self.client.get(self.url)

        data = {'detail': 'Method "GET" not allowed.'}

        self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)
        self.assertDictEqual(data, response.json())

    def test_missing_fields(self):

        data = {
            "username": "Test User Name",
            "email": "test@test.com",
            "phone": "+0000000000"
        }

        response = self.client.post(self.url, data=data)

        data = {"password": ["This field is required."]}

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertDictEqual(data, response.json())

    def test_invalid_email_address(self):

        data = {
            "username": "Test User Name",
            "email": "test",
            "phone": "+0000000000",
            "password": "Password"
        }

        response = self.client.post(self.url, data=data)

        data = {"email": ["Enter a valid email address."]}

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertDictEqual(data, response.json())

    def test_already_registered_email(self):
        user = mixer.blend('users.user')

        data = {
            "username": "Test User Name",
            "email": user.email,
            "phone": "+0000000000",
            "password": "Password"
        }

        response = self.client.post(self.url, data=data)

        data = {"email": ["user with this email address already exists."]}

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertDictEqual(data, response.json())

    def test_success_create(self):
        data = {
            "username": "Test User Name",
            "email": "test@test.com",
            "phone": "+0000000000",
            "password": "Password"
        }

        response = self.client.post(self.url, data=data)

        data = {
            "username": data["username"],
            "email": data["email"],
            "phone": data["phone"]
        }

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertDictEqual(data, response.json())