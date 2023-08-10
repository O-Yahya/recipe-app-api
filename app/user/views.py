"""
Views for User API.
"""
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in system."""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# Creating new view based on default view
# for updating objects
class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    # Settings authentication method to token authentication
    authentication_classes = [authentication.TokenAuthentication]
    # Giving authenticated users all permissions
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user
