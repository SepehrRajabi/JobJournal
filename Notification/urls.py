from django.urls import path

from .views import UserUnreadNotificationsListAPIView

app_name = "User"

urlpatterns = [
    path(
        "unread-notifications/",
        UserUnreadNotificationsListAPIView.as_view(),
        name="user-unread-notifications-list",
    )
]
