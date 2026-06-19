from django.contrib import admin

from .models import AssetType, Document, AssetGroup


class AssetTypeInAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]

    search_fields = [
        "name",
    ]

    list_filter = ["name"]


admin.site.register(AssetType, AssetTypeInAdmin)


class DocumentInAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "asset_type",
    ]


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
