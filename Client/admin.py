from django.contrib import admin

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


admin.site.register(Client, ClientInAdmin)
