from django.shortcuts import render
from rest_framework import generics

from user.serializers import UserSerializer

# Create your views here.


class CreateUserView(generics.CreateAPIView):
    """
        Creates a new user in the database
    """
    serializer_class = UserSerializer
