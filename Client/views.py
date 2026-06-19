from rest_framework import generics

from .models import Client, ClientContactInfo, ClientType
from .serializers import (
    ClientContactInfoCreateSerializer,
    ClientContactInfoDeleteSerializer,
    ClientContactInfoDetailSerializer,
    ClientContactInfosListSerializer,
    ClientContactInfoUpdateSerializer,
    ClientCreateSerializer,
    ClientDeleteSerializer,
    ClientDetailSerializer,
    ClientsListSerializer,
    ClientTypeCreateSerializer,
    ClientTypeDeleteSerializer,
    ClientTypeDetailSerializer,
    ClientTypesListSerializer,
    ClientTypeUpdateSerializer,
    ClientUpdateSerializer,
)


class ClientTypeDetailAPIView(generics.RetrieveAPIView):
    queryset = ClientType.objects.all()
    serializer_class = ClientTypeDetailSerializer


class ClientTypesListAPIView(generics.ListAPIView):
    queryset = ClientType.objects.all()
    serializer_class = ClientTypesListSerializer


class ClientTypeCreateAPIView(generics.CreateAPIView):
    queryset = ClientType.objects.all()
    serializer_class = ClientTypeCreateSerializer


class ClientTypeUpdateAPIView(generics.UpdateAPIView):
    queryset = ClientType.objects.all()
    serializer_class = ClientTypeUpdateSerializer


class ClientTypeDeleteAPIView(generics.DestroyAPIView):
    queryset = ClientType.objects.all()
    serializer_class = ClientTypeDeleteSerializer


class ClientContactInfoDetailAPIView(generics.RetrieveAPIView):
    queryset = ClientContactInfo.objects.all()
    serializer_class = ClientContactInfoDetailSerializer


class ClientContactInfosListAPIView(generics.ListAPIView):
    queryset = ClientContactInfo.objects.all()
    serializer_class = ClientContactInfosListSerializer


class ClientContactInfoCreateAPIView(generics.CreateAPIView):
    queryset = ClientContactInfo.objects.all()
    serializer_class = ClientContactInfoCreateSerializer


class ClientContactInfoUpdateAPIView(generics.UpdateAPIView):
    queryset = ClientContactInfo.objects.all()
    serializer_class = ClientContactInfoUpdateSerializer


class ClientContactInfoDeleteAPIView(generics.DestroyAPIView):
    queryset = ClientContactInfo.objects.all()
    serializer_class = ClientContactInfoDeleteSerializer


class ClientDetailAPIView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer


class ClientsListAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientsListSerializer


class ClientCreateAPIView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer


class ClientUpdateAPIView(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientUpdateSerializer


class ClientDeleteAPIView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDeleteSerializer
