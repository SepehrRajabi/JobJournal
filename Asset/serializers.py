from rest_framework import serializers

from .models import AssetGroup, AssetType, Document


class AssetTypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetType
        fields = ["id", "name", "created_at", "updated_at"]


class AssetTypesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetType
        fields = ["id", "name", "created_at", "updated_at"]


class AssetTypeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetType
        fields = ["id", "name", "created_at", "updated_at"]


class AssetTypeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetType
        fields = ["id", "name", "created_at", "updated_at"]


class AssetTypeDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetType
        fields = ["id"]


class DocumentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [
            "id",
            "title",
            "user",
            "asset_type",
            "file",
            "created_at",
            "updated_at",
        ]


class DocumentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [
            "id",
            "title",
            "user",
            "asset_type",
            "file",
            "created_at",
            "updated_at",
        ]


class DocumentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [
            "id",
            "title",
            "user",
            "asset_type",
            "file",
            "created_at",
            "updated_at",
        ]


class DocumentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [
            "id",
            "title",
            "user",
            "asset_type",
            "file",
            "created_at",
            "updated_at",
        ]


class DocumentDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ["id"]


class AssetGroupDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetGroup
        fields = ["id", "name", "assets", "created_at", "updated_at"]


class AssetGroupsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetGroup
        fields = ["id", "name", "assets", "created_at", "updated_at"]


class AssetGroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetGroup
        fields = ["id", "name", "assets", "created_at", "updated_at"]


class AssetGroupUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetGroup
        fields = ["id", "name", "assets", "created_at", "updated_at"]


class AssetGroupDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetGroup
        fields = ["id"]
