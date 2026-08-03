from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission

from JobApplication.models import (
    JobApplication,
)

User = get_user_model()


# admin.site.__class__ = OTPAdminSite


admin.site.site_title = "JobJournal Site Admin (DEV)"
admin.site.site_header = "JobJournal Administration"
admin.site.index_title = "JobJournal Site"


class JobApplicationInline(admin.StackedInline):
    model = JobApplication
    extra = 1
    readonly_fields = (
        "id",
        "created_at",
    )
    can_delete = False
    show_change_link = True


class UserInAdmin(UserAdmin):
    search_fields = [
        "first_name",
        "last_name",
    ]

    list_display = [
        "id",
        "first_name",
        "last_name",
    ]

    list_filter = [
        "is_superuser",
        "is_active",
    ]

    readonly_fields = ("last_login",)

    fieldsets = (
        (
            "General Information",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "password",
                )
            },
        ),
        ("Contact", {"fields": ("email",)}),
        (
            "Account Status",
            {
                "fields": (
                    "is_active",
                    "is_admin",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (
            "Permissions and Groups",
            {
                "fields": (
                    "user_permissions",
                    "groups",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            "None",
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                )
            },
        ),
    )

    ordering = ("-last_name",)
    filter_horizontal = ()

    inlines = [JobApplicationInline]


admin.site.register(User, UserInAdmin)

admin.site.register(Permission)
