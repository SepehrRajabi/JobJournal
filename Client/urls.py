from django.urls import path

from .views import (
    ClientContactInfoCreateAPIView,
    ClientContactInfoDeleteAPIView,
    ClientContactInfoDetailAPIView,
    ClientContactInfosListAPIView,
    ClientContactInfoUpdateAPIView,
    ClientCreateAPIView,
    ClientDeleteAPIView,
    ClientDetailAPIView,
    ClientsListAPIView,
    ClientTypeCreateAPIView,
    ClientTypeDeleteAPIView,
    ClientTypeDetailAPIView,
    ClientTypesListAPIView,
    ClientTypeUpdateAPIView,
    ClientUpdateAPIView,
)

app_name = "Client"

urlpatterns = [
    path("client-types/", ClientTypesListAPIView.as_view(), name="client-types-list"),
    path(
        "client-types/create/",
        ClientTypeCreateAPIView.as_view(),
        name="client-type-create",
    ),
    path(
        "client-types/<uuid:pk>/",
        ClientTypeDetailAPIView.as_view(),
        name="client-type-detail",
    ),
    path(
        "client-types/update/<uuid:pk>/",
        ClientTypeUpdateAPIView.as_view(),
        name="client-type-update",
    ),
    path(
        "client-types/delete/<uuid:pk>/",
        ClientTypeDeleteAPIView.as_view(),
        name="client-type-delete",
    ),
    path(
        "contact-infos/",
        ClientContactInfosListAPIView.as_view(),
        name="client-contact-infos-list",
    ),
    path(
        "contact-infos/create/",
        ClientContactInfoCreateAPIView.as_view(),
        name="client-contact-info-create",
    ),
    path(
        "contact-infos/<uuid:pk>/",
        ClientContactInfoDetailAPIView.as_view(),
        name="client-contact-info-detail",
    ),
    path(
        "contact-infos/update/<uuid:pk>/",
        ClientContactInfoUpdateAPIView.as_view(),
        name="client-contact-info-update",
    ),
    path(
        "contact-infos/delete/<uuid:pk>/",
        ClientContactInfoDeleteAPIView.as_view(),
        name="client-contact-info-delete",
    ),
    path("clients/", ClientsListAPIView.as_view(), name="clients-list"),
    path(
        "clients/create/",
        ClientCreateAPIView.as_view(),
        name="client-create",
    ),
    path(
        "clients/<uuid:pk>/",
        ClientDetailAPIView.as_view(),
        name="client-detail",
    ),
    path(
        "clients/update/<uuid:pk>/",
        ClientUpdateAPIView.as_view(),
        name="client-update",
    ),
    path(
        "clients/delete/<uuid:pk>/",
        ClientDeleteAPIView.as_view(),
        name="client-delete",
    ),
]
