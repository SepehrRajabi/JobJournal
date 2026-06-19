from rest_framework import generics

from .models import User
from .serializers import (
    UserCreateSerializer,
    UserDeleteSerializer,
    UserDetailSerializer,
    UsersListSerializer,
    UserUpdateSerializer,
)


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UsersListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersListSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer
