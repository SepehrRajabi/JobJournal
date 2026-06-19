from rest_framework import generics

from .models import AssetGroup, AssetType, Document
from .serializers import (
    AssetGroupCreateSerializer,
    AssetGroupDeleteSerializer,
    AssetGroupDetailSerializer,
    AssetGroupsListSerializer,
    AssetGroupUpdateSerializer,
    AssetTypeCreateSerializer,
    AssetTypeDeleteSerializer,
    AssetTypeDetailSerializer,
    AssetTypesListSerializer,
    AssetTypeUpdateSerializer,
    DocumentCreateSerializer,
    DocumentDeleteSerializer,
    DocumentDetailSerializer,
    DocumentsListSerializer,
    DocumentUpdateSerializer,
)


class AssetTypeDetailAPIView(generics.RetrieveAPIView):
    queryset = AssetType.objects.all()
    serializer_class = AssetTypeDetailSerializer


class AssetTypesListAPIView(generics.ListAPIView):
    queryset = AssetType.objects.all()
    serializer_class = AssetTypesListSerializer


class AssetTypeCreateAPIView(generics.CreateAPIView):
    queryset = AssetType.objects.all()
    serializer_class = AssetTypeCreateSerializer


class AssetTypeUpdateAPIView(generics.UpdateAPIView):
    queryset = AssetType.objects.all()
    serializer_class = AssetTypeUpdateSerializer


class AssetTypeDeleteAPIView(generics.DestroyAPIView):
    queryset = AssetType.objects.all()
    serializer_class = AssetTypeDeleteSerializer


class DocumentDetailAPIView(generics.RetrieveAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentDetailSerializer


class DocumentsListAPIView(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentsListSerializer


class DocumentCreateAPIView(generics.CreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentCreateSerializer


class DocumentUpdateAPIView(generics.UpdateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentUpdateSerializer


class DocumentDeleteAPIView(generics.DestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentDeleteSerializer


class AssetGroupDetailAPIView(generics.RetrieveAPIView):
    queryset = AssetGroup.objects.all()
    serializer_class = AssetGroupDetailSerializer


class AssetGroupsListAPIView(generics.ListAPIView):
    queryset = AssetGroup.objects.all()
    serializer_class = AssetGroupsListSerializer


class AssetGroupCreateAPIView(generics.CreateAPIView):
    queryset = AssetGroup.objects.all()
    serializer_class = AssetGroupCreateSerializer


class AssetGroupUpdateAPIView(generics.UpdateAPIView):
    queryset = AssetGroup.objects.all()
    serializer_class = AssetGroupUpdateSerializer


class AssetGroupDeleteAPIView(generics.DestroyAPIView):
    queryset = AssetGroup.objects.all()
    serializer_class = AssetGroupDeleteSerializer
