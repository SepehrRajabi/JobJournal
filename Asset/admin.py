from django.contrib import admin

from .models import AssetExtension, AssetGroup, AssetType, Document, VersionedDocument


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
        "asset_type",
        "user",
        "created_at",
        "updated_at",
    ]


admin.site.register(Document, DocumentInAdmin)


class VersionedDocumentInAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "document",
        "created_at",
    ]

    ordering = ["created_at"]


admin.site.register(VersionedDocument, VersionedDocumentInAdmin)


class AssetGroupInAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]

    search_fields = [
        "name",
    ]

    # filter_horizontal = ["assets"]


admin.site.register(AssetGroup, AssetGroupInAdmin)
