from drf_spectacular.utils import OpenApiParameter, OpenApiTypes, extend_schema
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


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="title",
            type=OpenApiTypes.STR,
            description="Title of the Client Type",
        ),
    ]
)
class ClientTypesListAPIView(generics.ListAPIView):
    serializer_class = ClientTypesListSerializer

    def get_queryset(self):
        client_types = ClientType.objects.all()

        if title := self.request.query_params.get("title"):
            client_types = client_types.filter(title=title)

        return client_types


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


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="website",
            type=OpenApiTypes.STR,
            description="Website of the Client Contact Info",
        ),
        OpenApiParameter(
            name="linkedin",
            type=OpenApiTypes.STR,
            description="LinkedIn of the Client Contact Info",
        ),
        OpenApiParameter(
            name="email",
            type=OpenApiTypes.STR,
            description="Email of the Client Contact Info",
        ),
        OpenApiParameter(
            name="phone",
            type=OpenApiTypes.STR,
            description="Phone of the Client Contact Info",
        ),
    ]
)
class ClientContactInfosListAPIView(generics.ListAPIView):
    serializer_class = ClientContactInfosListSerializer

    def get_queryset(self):
        contact_infos = ClientContactInfo.objects.all()

        if website := self.request.query_params.get("website"):
            contact_infos = contact_infos.filter(website=website)

        if linkedin := self.request.query_params.get("linkedin"):
            contact_infos = contact_infos.filter(linkedin=linkedin)

        if email := self.request.query_params.get("email"):
            contact_infos = contact_infos.filter(email=email)

        if phone := self.request.query_params.get("phone"):
            contact_infos = contact_infos.filter(phone=phone)

        return contact_infos


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


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="name",
            type=OpenApiTypes.STR,
            description="Name of the Client",
        ),
        OpenApiParameter(
            name="type",
            type=OpenApiTypes.UUID,
            description="Client Type ID of the Client",
        ),
    ]
)
class ClientsListAPIView(generics.ListAPIView):
    serializer_class = ClientsListSerializer

    def get_queryset(self):
        clients = Client.objects.all()

        if name := self.request.query_params.get("name"):
            clients = clients.filter(name=name)

        if type_id := self.request.query_params.get("type"):
            clients = clients.filter(type__id=type_id)

        return clients


class ClientCreateAPIView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer


class ClientUpdateAPIView(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientUpdateSerializer


class ClientDeleteAPIView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDeleteSerializer
