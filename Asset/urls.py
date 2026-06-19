from django.urls import path

from .views import (
    AssetGroupCreateAPIView,
    AssetGroupDeleteAPIView,
    AssetGroupDetailAPIView,
    AssetGroupsListAPIView,
    AssetGroupUpdateAPIView,
    AssetTypeCreateAPIView,
    AssetTypeDeleteAPIView,
    AssetTypeDetailAPIView,
    AssetTypesListAPIView,
    AssetTypeUpdateAPIView,
    DocumentCreateAPIView,
    DocumentDeleteAPIView,
    DocumentDetailAPIView,
    DocumentsListAPIView,
    DocumentUpdateAPIView,
)

app_name = "Asset"

urlpatterns = [
    path("asset-types/", AssetTypesListAPIView.as_view(), name="asset-types-list"),
    path(
        "asset-types/create/",
        AssetTypeCreateAPIView.as_view(),
        name="asset-type-create",
    ),
    path(
        "asset-types/<uuid:pk>/",
        AssetTypeDetailAPIView.as_view(),
        name="asset-type-detail",
    ),
    path(
        "asset-types/update/<uuid:pk>/",
        AssetTypeUpdateAPIView.as_view(),
        name="asset-type-update",
    ),
    path(
        "asset-types/delete/<uuid:pk>/",
        AssetTypeDeleteAPIView.as_view(),
        name="asset-type-delete",
    ),
    path("documents/", DocumentsListAPIView.as_view(), name="documents-list"),
    path(
        "documents/create/",
        DocumentCreateAPIView.as_view(),
        name="document-create",
    ),
    path(
        "documents/<uuid:pk>/",
        DocumentDetailAPIView.as_view(),
        name="document-detail",
    ),
    path(
        "documents/update/<uuid:pk>/",
        DocumentUpdateAPIView.as_view(),
        name="document-update",
    ),
    path(
        "documents/delete/<uuid:pk>/",
        DocumentDeleteAPIView.as_view(),
        name="document-delete",
    ),
    path("asset-groups/", AssetGroupsListAPIView.as_view(), name="asset-groups-list"),
    path(
        "asset-groups/create/",
        AssetGroupCreateAPIView.as_view(),
        name="asset-group-create",
    ),
    path(
        "asset-groups/<uuid:pk>/",
        AssetGroupDetailAPIView.as_view(),
        name="asset-group-detail",
    ),
    path(
        "asset-groups/update/<uuid:pk>/",
        AssetGroupUpdateAPIView.as_view(),
        name="asset-group-update",
    ),
    path(
        "asset-groups/delete/<uuid:pk>/",
        AssetGroupDeleteAPIView.as_view(),
        name="asset-group-delete",
    ),
]
