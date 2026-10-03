from django.contrib import admin

from .models import Notification, NotificationDispatch


class NotificationDispatchInline(admin.TabularInline):
    model = NotificationDispatch
    extra = 0
    fields = ["recipient", "created_at", "read_at"]
    readonly_fields = ["created_at"]
    autocomplete_fields = ["recipient"]
    ordering = ["-created_at"]


class NotificationInAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "action",
        "subject_type",
        "subject_id",
        "object_type",
        "object_id",
        "created_at",
    ]
    list_filter = [
        "action",
        "subject_type",
        "object_type",
        ("created_at", admin.DateFieldListFilter),
    ]
    search_fields = ["message", "subject_id", "object_id"]
    readonly_fields = ["id", "created_at"]
    inlines = [NotificationDispatchInline]
    list_select_related = ["subject_type", "object_type"]
    ordering = ["-created_at"]


admin.site.register(Notification, NotificationInAdmin)


class NotificationDispatchInAdmin(admin.ModelAdmin):
    list_display = ["notification", "recipient", "created_at", "read_at"]
    list_filter = [
        ("created_at", admin.DateFieldListFilter),
        ("read_at", admin.DateFieldListFilter),
    ]
    search_fields = [
        "recipient__first_name",
        "recipient__last_name",
        "recipient__email",
        "notification__message",
    ]
    autocomplete_fields = ["recipient", "notification"]
    readonly_fields = ["id", "created_at"]
    list_select_related = ["recipient", "notification"]
    ordering = ["-created_at"]


admin.site.register(NotificationDispatch, NotificationDispatchInAdmin)
