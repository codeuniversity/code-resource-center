from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email, password,
        first and last name is successful"""
        email = 'dani@code.berlin'
        password = 'password123'
        first_name = 'Dani'
        last_name = 'Santos'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password, password)
        self.assertEqual(user.first_name, first_name)
        self.assertTrue(user.last_name, last_name)
