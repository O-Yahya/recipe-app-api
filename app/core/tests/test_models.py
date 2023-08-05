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

    def test_new_user_email_normalized(self):
        """Test email is normalized for users"""
        # Test data for emails before and after normalization
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        # Check that email is normalized as expected
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'sample23')
