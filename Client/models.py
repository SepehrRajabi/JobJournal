from uuid import uuid4

from django.core.validators import RegexValidator
from django.db import models
from django.db.models import CheckConstraint, Q, UniqueConstraint


class ClientType(models.Model):
    id = models.UUIDField(
        default=uuid4,
        editable=False,
        null=False,
        primary_key=True,
        unique=True,
        db_index=True,
    )
    title = models.CharField(max_length=200, unique=True)
    # company
    # individual
    # agency
    # government
    # nonprofit
    # startup
    # other

    def __str__(self):
        return f"{self.title}"


class ClientContactInfo(models.Model):
    id = models.UUIDField(
        default=uuid4,
        editable=False,
        null=False,
        primary_key=True,
        unique=True,
        db_index=True,
    )
    website = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                regex=r"^\d+$",
                message="Phone number must contain only digits.",
            )
        ],
    )
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            UniqueConstraint(
                name="unique_website",
                fields=["website"],
                condition=Q(website__isnull=False),
            ),
            UniqueConstraint(
                name="unique_linkedin",
                fields=["linkedin"],
                condition=Q(linkedin__isnull=False),
            ),
            UniqueConstraint(
                name="unique_email",
                fields=["email"],
                condition=Q(email__isnull=False),
            ),
            CheckConstraint(
                condition=~(
                    Q(website__isnull=True)
                    & Q(linkedin__isnull=True)
                    & Q(email__isnull=True)
                ),
                name="at_least_one_info",
            ),
        ]

    def __str__(self):
        return f"{self.website}"


class Client(models.Model):
    id = models.UUIDField(
        default=uuid4,
        editable=False,
        null=False,
        primary_key=True,
        unique=True,
        db_index=True,
    )
    name = models.CharField(max_length=200, unique=True)
    contact_info = models.OneToOneField(
        ClientContactInfo, null=True, blank=True, on_delete=models.SET_NULL
    )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
