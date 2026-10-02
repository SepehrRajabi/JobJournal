from rest_framework import serializers
from rest_framework.fields import UUIDField

from .models import Client, ClientContactInfo, ClientType


class ClientTypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientType
        fields = ["id", "title"]


class ClientTypesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientType
        fields = ["id", "title"]


class ClientTypeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientType
        fields = ["id", "title"]


class ClientTypeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientType
        fields = ["id", "title"]


class ClientTypeDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientType
        fields = ["id"]


class ClientContactInfoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContactInfo
        fields = ["id", "website", "linkedin", "email", "phone", "created_at"]


class ClientContactInfosListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContactInfo
        fields = ["id", "website", "linkedin", "email", "phone", "created_at"]


class ClientContactInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContactInfo
        fields = ["id", "website", "linkedin", "email", "phone", "created_at"]


class ClientContactInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContactInfo
        fields = ["id", "website", "linkedin", "email", "phone", "created_at"]


class ClientContactInfoDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContactInfo
        fields = ["id"]


class ClientDetailSerializer(serializers.ModelSerializer):
    type = ClientTypeDetailSerializer()

    class Meta:
        model = Client
        fields = ["id", "name", "type", "contact_info", "created_at"]


class ClientsListSerializer(serializers.ModelSerializer):
    type = ClientTypeDetailSerializer()

    class Meta:
        model = Client
        fields = ["id", "name", "type", "contact_info", "created_at"]


class ClientCreateSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(
        queryset=ClientType.objects.all(),
        required=False,
        allow_null=True,
        pk_field=UUIDField(format="hex_verbose"),
    )

    class Meta:
        model = Client
        fields = ["id", "name", "type", "contact_info", "created_at"]


class ClientUpdateSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(
        queryset=ClientType.objects.all(),
        required=False,
        allow_null=True,
        pk_field=UUIDField(format="hex_verbose"),
    )

    class Meta:
        model = Client
        fields = ["id", "name", "type", "contact_info", "created_at"]


class ClientDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id"]
