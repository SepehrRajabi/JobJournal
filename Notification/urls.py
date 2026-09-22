from django.urls import path

from .views import UserNotificationsListAPIView

app_name = "User"

urlpatterns = [
    path(
        "unread-notifications/",
        UserNotificationsListAPIView.as_view(),
        name="user-unread-notifications-list",
    )
]
