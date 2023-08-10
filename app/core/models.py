"""
Database models.
"""
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return user"""
        # Raise exception if user created without email
        if not email:
            raise ValueError('User must have an email address.')
        # Creating a new user with given user data
        user = self.model(email=self.normalize_email(email), **extra_fields)
        # Setting given password using set_password to encrypt it
        user.set_password(password)
        # Saving user to database
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Defining custom user model"""
    # User database model fields
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Assigning UserManager class as manager for User class
    objects = UserManager()

    # Setting default USERNAME_FIELD to email field
    USERNAME_FIELD = 'email'


class Recipe(models.Model):
    """Recipe object"""
    # Recipe database model fields
    # User field to store user which recipe belongs to
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        # Setting the recipe to be deleted if the user is deleted
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)

    def __str__(self):
        """Return string representation"""
        return self.title
