from django.db.models import F
from rest_framework.generics import ListAPIView

from .models import NotificationDispatch
from .serializers import DispatchedNotificationSerializer


class UserNotificationsListAPIView(ListAPIView):
    """
    API view to retrieve a list of notifications for the authenticated user.
    """

    serializer_class = DispatchedNotificationSerializer

    def get_queryset(self):
        """
        Return the notifications for the authenticated user.
        """
        return NotificationDispatch.objects.filter(
            user=self.request.user, read_at__isnull=True
        ).order_by(F("created_at").desc(nulls_last=True))
