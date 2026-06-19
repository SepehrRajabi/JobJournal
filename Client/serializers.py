from rest_framework import serializers

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
        fields = ["id", "title"]


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
        fields = ["id", "website", "linkedin", "email", "phone", "created_at"]


class ClientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "name", "contact_info", "created_at"]


class ClientsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "name", "contact_info", "created_at"]


class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "name", "contact_info", "created_at"]


class ClientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "name", "contact_info", "created_at"]


class ClientDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "name", "contact_info", "created_at"]
