from uuid import uuid4

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import F


def create_asset_upload_path(instance, filename):
    return f"assets/{filename}"


class AssetExtension(models.Model):
    id = models.UUIDField(
        default=uuid4,
        editable=False,
        null=False,
        primary_key=True,
        unique=True,
        db_index=True,
    )
    extension = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.extension.startswith("."):
            self.extension = self.extension.replace(".", "", count=1)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        if self.extension.startswith("."):
            return f"{self.extension.replace('.', '', count=1)}"
        return f"{self.extension}"


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
    supported_extensions = models.ManyToManyField(
        AssetExtension, related_name="asset_types", blank=True
    )
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
        AssetType,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="documents",
    )
    # The versioned "slot" this document is a version of (e.g. "CV"). A
    # document belongs to at most one group; created_at is what orders
    # versions within it - see AssetGroup.get_latest_version().
    asset_group = models.ForeignKey(
        "AssetGroup",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="documents",
    )
    file = models.FileField(null=True, blank=True, upload_to=create_asset_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.file.name} {self.user.first_name} {self.user.last_name}"

    def save(self, *args, **kwargs):
        extension = self.file.name.split(".")[-1]
        if extension not in self.asset_type.supported_extensions.values_list(
            "extension", flat=True
        ):
            raise ValidationError(
                "Uploaded file's extension does not belong to the specified asset type"
            )

        super().save(*args, **kwargs)


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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    def get_latest_version(self) -> Document | None:
        return self.documents.order_by(F("created_at").desc()).first()
