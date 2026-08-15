from uuid import uuid4

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Notification(models.Model):
    class ActionChoices(models.TextChoices):
        # TICKET_CREATE = "ticket_create", "ticket_create"
        # TICKET_STATUS_CHANGE = "ticket_status_change", "ticket_status_change"

        # TICKET_POST_CREATE = "ticket_post_create", "ticket_post_create"

        # TASK_CREATE = "task_create", "task_create"
        # TASK_STATUS_CHANGE = "task_status_change", "task_status_change"
        # TASK_ASSIGNEE_CHANGE = "task_assignee_change", "task_assignee_change"

        # TASK_COMMENT_CREATE = "task_comment_create", "task_comment_create"
        # TASK_COMMENT_SEEN = "task_comment_seen", "task_comment_seen"
        # TODO: add all the possible action choices.
        pass

    id = models.UUIDField(
        default=uuid4,
        editable=False,
        null=False,
        primary_key=True,
        unique=True,
        db_index=True,
    )
    object_type = models.ForeignKey(
        ContentType,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="object_notifications",
    )
    object_id = models.CharField(null=True, blank=True)
    object = GenericForeignKey(ct_field="object_type", fk_field="object_id")

    subject_type = models.ForeignKey(
        ContentType,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="subject_notifications",
    )
    subject_id = models.CharField(null=True, blank=True)
    subject = GenericForeignKey(ct_field="subject_type", fk_field="subject_id")

    action = models.CharField(null=True, blank=True, choices=ActionChoices)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject_type} - {self.subject_id}"


class NotificationDispatch(models.Model):
    id = models.UUIDField(
        default=uuid4,
        editable=False,
        null=False,
        primary_key=True,
        unique=True,
        db_index=True,
    )
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="dispatched_notifications",
    )
    notification = models.ForeignKey(
        Notification,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="dispatches",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True)

    class Meta:
        unique_together = ["recipient", "notification"]
        verbose_name_plural = "Notification Dispatches"

    def __str__(self):
        return f"{self.notification}"
