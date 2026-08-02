from django.contrib.auth.models import Permission
from django.db.models import Q
from django.db.models.base import Model
from django.views.generic import View
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission

from User.models import User


class BaseResourcePermission(BasePermission):
    def _method_to_action(self, method: str) -> str:
        mapping = {
            "GET": "retrieve",
            "POST": "create",
            "PUT": "update",
            "PATCH": "partial_update",
            "DELETE": "destroy",
        }

        if method.upper() not in mapping:
            raise ValueError(f"Unknown method: {method}")

        return mapping[method.upper()]

    def _get_model_from_view(self, view: View) -> Model | None:
        return (
            getattr(view, "permission_model", None)
            or getattr(view, "queryset", None)
            or getattr(view, "get_queryset", None)
            or getattr(view, "serializer_class", None)
        ).model

    def get_action_and_model(self, view: View) -> tuple[str, Model]:
        action = getattr(view, "action", None)

        if action is None:
            action = self._method_to_action(view.request.method)

        model = self._get_model_from_view(view)

        if model is None:
            raise PermissionDenied("Could not determine resource type.")

        return action, model

    def has_permission(self, request, view) -> bool:
        user = request.user

        if not user or not user.is_authenticated:
            raise PermissionDenied("Authentication required.")

        action, model = self.get_action_and_model(view)

        if model is None:
            raise PermissionDenied("Could not determine resource type.")

        if action == "unknown":
            raise PermissionDenied(f"Method {request.method} not allowed.")

        required = self.build_required_permission(action, model)

        user_perms = self.get_user_permissions(user)

        if required not in user_perms:
            raise PermissionDenied(
                f"Permission '{required}' required for {action} on {model.__name__}."
            )

        return True

    def build_required_permission(self, action: str, model: Model) -> str:
        action_to_django = {
            "list": "view",
            "retrieve": "view",
            "create": "add",
            "update": "change",
            "partial_update": "change",
            "destroy": "delete",
        }

        app_label = model._meta.app_label
        model_name = model._meta.model_name

        django_action = action_to_django.get(action)

        if django_action is None:
            raise PermissionDenied(f"Unknown action: {action}")

        return f"{app_label}.{django_action}_{model_name}"

    def get_user_permissions(self, user: User) -> set[str]:
        perms = (
            Permission.objects.filter(Q(user=user) | Q(group__user=user))
            .values_list("content_type__app_label", "codename")
            .distinct()
        )

        return {f"{app}.{codename}" for app, codename in perms}
