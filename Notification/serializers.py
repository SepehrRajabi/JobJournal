from rest_framework import serializers
from users.serializers import UserDetailSerializer

from .models import NotificationDispatch


class DispatchedNotificationSerializer(serializers.ModelSerializer):
    recipient = UserDetailSerializer(read_only=True)
    """
    Serializer for the NotificationDispatch model.
    """

    class Meta:
        model = NotificationDispatch
        fields = ["id", "recipient", "notification", "created_at", "read_at"]
