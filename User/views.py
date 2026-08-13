from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

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
    permission_classes = [IsAuthenticated]
    serializer_class = UserDeleteSerializer

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)

    def get_object(self):
        return self.get_queryset().first()
