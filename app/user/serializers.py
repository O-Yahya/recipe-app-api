"""
Serializers for the user API View.
"""
from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""
    # Choose model this serializer is used for
    class Meta:
        model = get_user_model()
        fields = ('email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'},
                'min_length': 5
            }
        }

    def create(self, validated_data):
        """Create and return user with encrypted password"""
        # Override create method to use created create user method
        user = get_user_model().objects.create_user(**validated_data)
        return user
