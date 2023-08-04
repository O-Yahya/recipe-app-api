"""
Test custom models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating user with email is successful"""
        # Test data for creating a user
        email = 'test@example.com'
        password = 'testpass123'
        # Creating new user from our user model
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        # Asserstions
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
