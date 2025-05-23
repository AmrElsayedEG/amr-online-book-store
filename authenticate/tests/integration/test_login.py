from utils.test_utils import mixer, reverse, status, APITestCase

class LoginTestCase(APITestCase):

    def setUp(self):
        self.user = mixer.blend('users.user')
        self.url = reverse('authenticate:login')

    def test_method_not_allowed(self):

        response = self.client.get(self.url)

        data = {'detail': 'Method "GET" not allowed.'}

        self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)
        self.assertDictEqual(data, response.json())

    def test_missing_fields(self):

        data = {
            "email": "test@test.com"
        }

        response = self.client.post(self.url, data=data)

        data = {"password": ["This field is required."]}

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertDictEqual(data, response.json())

    def test_invalid_credentials(self):

        data = {
            "email": self.user.email,
            "password": "random_password_paymob"
        }

        response = self.client.post(self.url, data=data)

        data = {"error": ["Invalid Credentials"]}

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertDictEqual(data, response.json())

    def test_not_active(self):
        # Override the password to get the non encrypted pwd
        self.user.set_password('test_password')
        self.user.is_active = False
        self.user.save()

        data = {
            "email": self.user.email,
            "password": "test_password"
        }

        response = self.client.post(self.url, data=data)

        data = {"error": ["This account is not activated, Please contact the support."]}

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertDictEqual(data, response.json())

    def test_success(self):
        # Override the password to get the non encrypted pwd
        self.user.set_password('test_password')
        self.user.save()

        data = {
            "email": self.user.email,
            "password": "test_password"
        }

        response = self.client.post(self.url, data=data)

        self.assertEqual(status.HTTP_200_OK, response.status_code)