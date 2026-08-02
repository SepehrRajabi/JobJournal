from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        default=uuid4,
        editable=False,
        null=False,
        primary_key=True,
        unique=True,
        db_index=True,
    )

    # General information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    # Permissions
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]

    objects = UserManager()

    class Meta(AbstractBaseUser.Meta):
        swappable = "AUTH_USER_MODEL"
        ordering = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, *args, **kwargs):
        return super().has_perm(*args, **kwargs)

    def has_perms(self, *perms, obj=None):
        return all(self.has_perm(perm, obj) for perm in perms)

    # TODO: properly check the permissions
    def has_module_perms(self, app_label, *args, **kwargs):
        return True

    @property
    def jwt_tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh": f"{refresh}",
            "access": f"{refresh.access_token}",
        }
