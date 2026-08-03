from uuid import uuid4

from django.conf import settings
from django.db import models
from jsonschema import ValidationError


def create_asset_upload_path(instance, filename):
    return f"assets/{instance.file.name}"


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
        return super().save(*args, **kwargs)

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

        return super().save(*args, **kwargs)


class VersionedDocument(models.Model):
    id = models.UUIDField(
        default=uuid4,
        unique=True,
        editable=False,
        db_index=True,
        primary_key=True,
        null=False,
    )
    asset_group = models.ForeignKey(
        "AssetGroup",
        on_delete=models.CASCADE,
        related_name="asset_links",
    )
    document = models.ForeignKey(
        Document, on_delete=models.CASCADE, related_name="versions"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["asset_group", "document"],
                name="unique_asset_group_document",
            )
        ]

    def __str__(self) -> str:
        return f"{self.asset_group.name} - {self.document.title}"


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
    assets = models.ManyToManyField(
        Document,
        blank=True,
        through=VersionedDocument,
        through_fields=("asset_group", "document"),
        related_name="asset_groups",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
