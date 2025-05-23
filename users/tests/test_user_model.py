from utils.test_utils import mixer, TestCase
from users.models import User
from utils import UserTypeChoices

class UserModelTest(TestCase):

    def test_user_creation(self):
        user = mixer.blend('users.user')

        self.assertIsInstance(user, User)

        self.assertIsNotNone(user.id)
        self.assertEqual(user.email, str(user))

    def test_user_update_password(self):
        user = mixer.blend('users.user')
        
        user.set_password('new_password')
        user.save()

        self.assertTrue(user.check_password('new_password'))

    def test_user_creation_with_fields(self):
        user = User.objects.create_user(username='amr', email='paymob@amr.com', password='amr_test_pwd')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'paymob@amr.com')
        self.assertTrue(user.check_password('amr_test_pwd'))

    def test_user_type_default_is_customer(self):
        user = mixer.blend(User)
        self.assertEqual(user.user_type, UserTypeChoices.CUSTOMER)

    def test_superuser_creation(self):
        admin = User.objects.create_superuser(username='amr', email='paymob@amr.com', password='amr_test_pwd')
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)
        self.assertEqual(admin.email, 'paymob@amr.com')
        self.assertTrue(admin.check_password('amr_test_pwd'))

