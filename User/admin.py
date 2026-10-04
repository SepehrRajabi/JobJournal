from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
from django.urls import reverse
from django.utils.html import format_html_join

from JobApplication.models import (
    JobApplication,
    Offer,
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
    classes = ["collapse"]


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

    readonly_fields = ("last_login", "offers")

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
        (
            "Offers",
            {
                "fields": ("offers",),
                "classes": ("collapse",),
            },
        ),
    )

    @admin.display(description="Offers")
    def offers(self, obj):
        offers = Offer.objects.filter(application__user=obj).select_related(
            "application"
        )
        if not offers:
            return "—"

        return format_html_join(
            "",
            '<div><a href="{}">{}</a> — deadline: {}</div>',
            (
                (
                    reverse("admin:JobApplication_offer_change", args=[offer.pk]),
                    offer.application.title,
                    offer.decision_deadline or "—",
                )
                for offer in offers
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
