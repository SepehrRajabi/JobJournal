from rest_framework import generics

from .models import (
    InterviewResult,
    InterviewStage,
    InterviewStageStatus,
    InterviewStageType,
    JobApplication,
    JobApplicationStatus,
    Oppurtunity,
)
from .serializers import (
    InterviewResultCreateSerializer,
    InterviewResultDeleteSerializer,
    InterviewResultDetailSerializer,
    InterviewResultsListSerializer,
    InterviewResultUpdateSerializer,
    InterviewStageCreateSerializer,
    InterviewStageDeleteSerializer,
    InterviewStageDetailSerializer,
    InterviewStagesListSerializer,
    InterviewStageStatusCreateSerializer,
    InterviewStageStatusDeleteSerializer,
    InterviewStageStatusDetailSerializer,
    InterviewStageStatusesListSerializer,
    InterviewStageStatusUpdateSerializer,
    InterviewStageTypeCreateSerializer,
    InterviewStageTypeDeleteSerializer,
    InterviewStageTypeDetailSerializer,
    InterviewStageTypesListSerializer,
    InterviewStageTypeUpdateSerializer,
    InterviewStageUpdateSerializer,
    JobApplicationCreateSerializer,
    JobApplicationDeleteSerializer,
    JobApplicationDetailSerializer,
    JobApplicationsListSerializer,
    JobApplicationStatusCreateSerializer,
    JobApplicationStatusDeleteSerializer,
    JobApplicationStatusDetailSerializer,
    JobApplicationStatusesListSerializer,
    JobApplicationStatusUpdateSerializer,
    JobApplicationUpdateSerializer,
    OppurtunityCreateSerializer,
    OppurtunityDeleteSerializer,
    OppurtunityDetailSerializer,
    OppurtunitiesListSerializer,
    OppurtunityUpdateSerializer,
)


class OppurtunityDetailAPIView(generics.RetrieveAPIView):
    queryset = Oppurtunity.objects.all()
    serializer_class = OppurtunityDetailSerializer


class OppurtunitiesListAPIView(generics.ListAPIView):
    queryset = Oppurtunity.objects.all()
    serializer_class = OppurtunitiesListSerializer


class OppurtunityCreateAPIView(generics.CreateAPIView):
    queryset = Oppurtunity.objects.all()
    serializer_class = OppurtunityCreateSerializer


class OppurtunityUpdateAPIView(generics.UpdateAPIView):
    queryset = Oppurtunity.objects.all()
    serializer_class = OppurtunityUpdateSerializer


class OppurtunityDeleteAPIView(generics.DestroyAPIView):
    queryset = Oppurtunity.objects.all()
    serializer_class = OppurtunityDeleteSerializer


class JobApplicationStatusDetailAPIView(generics.RetrieveAPIView):
    queryset = JobApplicationStatus.objects.all()
    serializer_class = JobApplicationStatusDetailSerializer


class JobApplicationStatusesListAPIView(generics.ListAPIView):
    queryset = JobApplicationStatus.objects.all()
    serializer_class = JobApplicationStatusesListSerializer


class JobApplicationStatusCreateAPIView(generics.CreateAPIView):
    queryset = JobApplicationStatus.objects.all()
    serializer_class = JobApplicationStatusCreateSerializer


class JobApplicationStatusUpdateAPIView(generics.UpdateAPIView):
    queryset = JobApplicationStatus.objects.all()
    serializer_class = JobApplicationStatusUpdateSerializer


class JobApplicationStatusDeleteAPIView(generics.DestroyAPIView):
    queryset = JobApplicationStatus.objects.all()
    serializer_class = JobApplicationStatusDeleteSerializer


class JobApplicationDetailAPIView(generics.RetrieveAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationDetailSerializer


class JobApplicationsListAPIView(generics.ListAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationsListSerializer


class JobApplicationCreateAPIView(generics.CreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationCreateSerializer


class JobApplicationUpdateAPIView(generics.UpdateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationUpdateSerializer


class JobApplicationDeleteAPIView(generics.DestroyAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationDeleteSerializer


class InterviewStageStatusDetailAPIView(generics.RetrieveAPIView):
    queryset = InterviewStageStatus.objects.all()
    serializer_class = InterviewStageStatusDetailSerializer


class InterviewStageStatusesListAPIView(generics.ListAPIView):
    queryset = InterviewStageStatus.objects.all()
    serializer_class = InterviewStageStatusesListSerializer


class InterviewStageStatusCreateAPIView(generics.CreateAPIView):
    queryset = InterviewStageStatus.objects.all()
    serializer_class = InterviewStageStatusCreateSerializer


class InterviewStageStatusUpdateAPIView(generics.UpdateAPIView):
    queryset = InterviewStageStatus.objects.all()
    serializer_class = InterviewStageStatusUpdateSerializer


class InterviewStageStatusDeleteAPIView(generics.DestroyAPIView):
    queryset = InterviewStageStatus.objects.all()
    serializer_class = InterviewStageStatusDeleteSerializer


class InterviewStageTypeDetailAPIView(generics.RetrieveAPIView):
    queryset = InterviewStageType.objects.all()
    serializer_class = InterviewStageTypeDetailSerializer


class InterviewStageTypesListAPIView(generics.ListAPIView):
    queryset = InterviewStageType.objects.all()
    serializer_class = InterviewStageTypesListSerializer


class InterviewStageTypeCreateAPIView(generics.CreateAPIView):
    queryset = InterviewStageType.objects.all()
    serializer_class = InterviewStageTypeCreateSerializer


class InterviewStageTypeUpdateAPIView(generics.UpdateAPIView):
    queryset = InterviewStageType.objects.all()
    serializer_class = InterviewStageTypeUpdateSerializer


class InterviewStageTypeDeleteAPIView(generics.DestroyAPIView):
    queryset = InterviewStageType.objects.all()
    serializer_class = InterviewStageTypeDeleteSerializer


class InterviewResultDetailAPIView(generics.RetrieveAPIView):
    queryset = InterviewResult.objects.all()
    serializer_class = InterviewResultDetailSerializer


class InterviewResultsListAPIView(generics.ListAPIView):
    queryset = InterviewResult.objects.all()
    serializer_class = InterviewResultsListSerializer


class InterviewResultCreateAPIView(generics.CreateAPIView):
    queryset = InterviewResult.objects.all()
    serializer_class = InterviewResultCreateSerializer


class InterviewResultUpdateAPIView(generics.UpdateAPIView):
    queryset = InterviewResult.objects.all()
    serializer_class = InterviewResultUpdateSerializer


class InterviewResultDeleteAPIView(generics.DestroyAPIView):
    queryset = InterviewResult.objects.all()
    serializer_class = InterviewResultDeleteSerializer


class InterviewStageDetailAPIView(generics.RetrieveAPIView):
    queryset = InterviewStage.objects.all()
    serializer_class = InterviewStageDetailSerializer


class InterviewStagesListAPIView(generics.ListAPIView):
    queryset = InterviewStage.objects.all()
    serializer_class = InterviewStagesListSerializer


class InterviewStageCreateAPIView(generics.CreateAPIView):
    queryset = InterviewStage.objects.all()
    serializer_class = InterviewStageCreateSerializer


class InterviewStageUpdateAPIView(generics.UpdateAPIView):
    queryset = InterviewStage.objects.all()
    serializer_class = InterviewStageUpdateSerializer


class InterviewStageDeleteAPIView(generics.DestroyAPIView):
    queryset = InterviewStage.objects.all()
    serializer_class = InterviewStageDeleteSerializer
