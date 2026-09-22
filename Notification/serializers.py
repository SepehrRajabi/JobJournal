from rest_framework import serializers

from .models import NotificationDispatch


class DispatchedNotificationSerializer(serializers.ModelSerializer):
    """
    Serializer for the NotificationDispatch model.
    """

    class Meta:
        model = NotificationDispatch
        fields = ["id", "recipient", "notification", "created_at", "read_at"]
