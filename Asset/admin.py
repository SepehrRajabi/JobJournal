from django.contrib import admin

from .models import AssetExtension, AssetGroup, AssetType, Document


class AssetExtensionInAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "extension",
    ]

    search_fields = [
        "extension",
    ]

    list_filter = ["extension"]

    ordering = ["created_at"]


admin.site.register(AssetExtension, AssetExtensionInAdmin)


class AssetTypeInAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]

    search_fields = [
        "name",
    ]

    filter_horizontal = ["supported_extensions"]

    ordering = ["created_at"]


admin.site.register(AssetType, AssetTypeInAdmin)


class DocumentInAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "asset_type",
        "asset_group",
        "user",
        "created_at",
        "updated_at",
    ]

    search_fields = [
        "title",
    ]

    autocomplete_fields = ["asset_group"]


admin.site.register(Document, DocumentInAdmin)


class AssetGroupInAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]

    search_fields = [
        "name",
    ]


admin.site.register(AssetGroup, AssetGroupInAdmin)
