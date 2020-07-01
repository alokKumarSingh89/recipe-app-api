from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """ User Modal Test Case"""

    def test_create_user_with_email(self):
        """Create USer With email and password only"""
        email = "alok@gmail.com"
        password = "password123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test user email noramlization"""
        email = "alok@GMAIL.COM"
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test For invalid email id"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test123')

    def test_create_new_superuser(self):
        """Create new Super user"""
        user = get_user_model().objects.create_superuser("alok@gmail.com", 'test1234')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
