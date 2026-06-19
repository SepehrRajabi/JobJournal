from django.urls import path

from .views import (
    UserCreateAPIView,
    UserDeleteAPIView,
    UserDetailAPIView,
    UsersListAPIView,
    UserUpdateAPIView,
)

app_name = "User"

urlpatterns = [
    path("users/", UsersListAPIView.as_view(), name="users-list"),
    path("users/create/", UserCreateAPIView.as_view(), name="user-create"),
    path("users/<uuid:pk>/", UserDetailAPIView.as_view(), name="user-detail"),
    path(
        "users/update/<uuid:pk>/",
        UserUpdateAPIView.as_view(),
        name="user-update",
    ),
    path(
        "users/delete/<uuid:pk>/",
        UserDeleteAPIView.as_view(),
        name="user-delete",
    ),
]
