from django.db import models
from django.conf import settings
from uuid import uuid4


def create_asset_upload_path(instance, filename):
    return f"assets/{instance.file.name}"


class AssetType(models.Model):
    id = models.UUIDField(
        default=uuid4,
        editable=False,
        null=False,
        primary_key=True,
        unique=True,
        db_index=True,
    )
    name = models.CharField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Document(models.Model):
    id = models.UUIDField(
        default=uuid4,
        editable=False,
        null=False,
        primary_key=True,
        unique=True,
        db_index=True,
    )
    title = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="documents",
    )

    asset_type = models.ForeignKey(
        AssetType, blank=True, null=True, on_delete=models.SET_NULL
    )
    file = models.FileField(null=True, blank=True, upload_to=create_asset_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.file.name}"


class AssetGroup(models.Model):
    id = models.UUIDField(
        default=uuid4,
        unique=True,
        editable=False,
        db_index=True,
        primary_key=True,
        null=False,
    )
    name = models.CharField(max_length=255, blank=True, null=True)
    assets = models.ManyToManyField(Document, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
