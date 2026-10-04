from django.contrib import admin

from JobApplication.models import JobApplication

from .models import Client, ClientContactInfo, ClientType


class ClientTypeInAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
    ]
    search_fields = [
        "title",
    ]


admin.site.register(ClientType, ClientTypeInAdmin)


class ClientContactInfoInAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "website",
        "email",
        "phone",
        "created_at",
    ]
    search_fields = [
        "website",
        "email",
        "phone",
    ]


admin.site.register(ClientContactInfo, ClientContactInfoInAdmin)


class JobApplicationInline(admin.TabularInline):
    model = JobApplication
    extra = 0
    fields = [
        "title",
        "status",
        "employment_type",
        "work_mode",
        "applied_at",
        "is_accepted",
    ]
    autocomplete_fields = ["status"]
    ordering = ["-created_at"]
    show_change_link = True


class ClientInAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "type",
        "contact_info",
        "created_at",
    ]
    list_filter = [
        "type",
    ]
    search_fields = [
        "name",
        "type__title",
        # "contact_info__website",
        # "contact_info__email",
        # "contact_info__phone",
    ]
    autocomplete_fields = ["type"]
    inlines = [JobApplicationInline]


admin.site.register(Client, ClientInAdmin)
