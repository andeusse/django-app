from rest_framework import generics

from user.serializers import UserSerlializer


class CreateUserView(generics.CreateAPIView):
    """Create new user in the system"""
    serializer_class = UserSerlializer
