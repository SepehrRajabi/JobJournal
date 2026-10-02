from django.db.models import Count, F
from django.utils import timezone
from drf_spectacular.utils import OpenApiParameter, OpenApiTypes, extend_schema
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import (
    InterviewResult,
    InterviewStage,
    InterviewStageStatus,
    InterviewStageType,
    JobApplication,
    JobApplicationStatus,
    Offer,
    Opportunity,
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
    JobApplicationDashboardSerializer,
    JobApplicationDeleteSerializer,
    JobApplicationDetailSerializer,
    JobApplicationsListSerializer,
    JobApplicationStatusCreateSerializer,
    JobApplicationStatusDeleteSerializer,
    JobApplicationStatusDetailSerializer,
    JobApplicationStatusesListSerializer,
    JobApplicationStatusUpdateSerializer,
    JobApplicationUpdateSerializer,
    OffersListSerializer,
    OpportunityCreateSerializer,
    OpportunityDeleteSerializer,
    OpportunityDetailSerializer,
    OpportunityUpdateSerializer,
    OppurtunitiesListSerializer,
)
from .utils import get_job_application_history


class OpportunityDetailAPIView(generics.RetrieveAPIView):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunityDetailSerializer


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="title",
            description="Title of the opportunity",
            type=OpenApiTypes.STR,
        )
    ]
)
class OppurtunitiesListAPIView(generics.ListAPIView):
    serializer_class = OppurtunitiesListSerializer

    def get_queryset(self):
        opportunities = Opportunity.objects.all()

        if title := self.request.query_params.get("title"):
            opportunities = opportunities.filter(title=title)

        return opportunities


class OpportunityCreateAPIView(generics.CreateAPIView):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunityCreateSerializer


class OpportunityUpdateAPIView(generics.UpdateAPIView):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunityUpdateSerializer


class OpportunityDeleteAPIView(generics.DestroyAPIView):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunityDeleteSerializer


class JobApplicationStatusDetailAPIView(generics.RetrieveAPIView):
    queryset = JobApplicationStatus.objects.all()
    serializer_class = JobApplicationStatusDetailSerializer


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="title",
            type=OpenApiTypes.STR,
            description="Title of the Job Application Status",
        ),
    ]
)
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


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="title",
            type=OpenApiTypes.STR,
            description="Title of the Job Application",
        ),
        OpenApiParameter(
            name="user",
            type=OpenApiTypes.UUID,
            description="User ID of the Job Application",
        ),
        OpenApiParameter(
            name="client",
            type=OpenApiTypes.UUID,
            description="Client ID of the Job Application",
        ),
        OpenApiParameter(
            name="opportunity",
            type=OpenApiTypes.UUID,
            description="Opportunity ID of the Job Application",
        ),
        OpenApiParameter(
            name="location",
            type=OpenApiTypes.STR,
            description="Location of the Job Application",
        ),
        OpenApiParameter(
            name="employment_type",
            type=OpenApiTypes.STR,
            description="Employment Type of the Job Application",
        ),
        OpenApiParameter(
            name="work_mode",
            type=OpenApiTypes.STR,
            description="Work Mode of the Job Application",
        ),
        OpenApiParameter(
            name="source",
            type=OpenApiTypes.STR,
            description="Source of the Job Application",
        ),
        OpenApiParameter(
            name="job_url",
            type=OpenApiTypes.STR,
            description="Job URL of the Job Application",
        ),
        OpenApiParameter(
            name="status",
            type=OpenApiTypes.UUID,
            description="Status ID of the Job Application",
        ),
        OpenApiParameter(
            name="applied_at_range",
            type=OpenApiTypes.DATE,
            description="Applied At date range of the Job Application",
        ),
    ]
)
class JobApplicationsListAPIView(generics.ListAPIView):
    serializer_class = JobApplicationsListSerializer

    def get_queryset(self):
        applications = JobApplication.objects.all()

        if title := self.request.query_params.get("title"):
            applications = applications.filter(title=title)

        if user_id := self.request.query_params.get("user"):
            applications = applications.filter(user__id=user_id)

        if client_id := self.request.query_params.get("client"):
            applications = applications.filter(client__id=client_id)

        if opportunity_id := self.request.query_params.get("opportunity"):
            applications = applications.filter(opportunity__id=opportunity_id)

        if location := self.request.query_params.get("location"):
            applications = applications.filter(location=location)

        return applications


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


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="scheduled_at",
            type=OpenApiTypes.DATETIME,
            description="The date the interview is scheduled for",
        ),
    ]
)
class UpcomingInterviewsListAPIView(generics.ListAPIView):
    serializer_class = InterviewStagesListSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        interviews = (
            InterviewStage.objects.select_related(
                "application", "stage_type", "status", "result"
            )
            .filter(
                application__user=self.request.user, scheduled_at__gte=timezone.now()
            )
            .order_by(F("scheduled_at").desc(nulls_last=True))
        )

        if scheduled_at := self.request.query_params.get("scheduled_at"):
            interviews = interviews.filter(scheduled_at=scheduled_at)

        return interviews


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="start_date",
            type=OpenApiTypes.DATE,
            description="Start date of the Offer",
        ),
        OpenApiParameter(
            name="decision_deadline",
            type=OpenApiTypes.DATE,
            description="Decision deadline of the Offer",
        ),
    ]
)
class UpcomingOffersListAPIView(generics.ListAPIView):
    serializer_class = OffersListSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        offers = (
            Offer.objects.select_related("application", "application__user")
            .filter(
                application__user=self.request.user,
                start_date__gte=timezone.localtime(timezone.now()).date(),
            )
            .order_by(F("start_date").asc(nulls_last=True))
        )

        if start_date := self.request.query_params.get("start_date"):
            offers = offers.filter(start_date=start_date)

        if decision_deadline := self.request.query_params.get("decision_deadline"):
            offers = offers.filter(decision_deadline=decision_deadline)

        return offers


class JobApplicationTimelineAPIView(generics.RetrieveAPIView):
    serializer_class = JobApplicationDetailSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return JobApplication.objects.filter(
            user=self.request.user, id=self.kwargs[self.lookup_field]
        )

    def get(self, request, *args, **kwargs):
        instance = self.get_queryset().first()

        if not instance:
            return Response(
                {"detail": "Job application not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            get_job_application_history(job_application=instance),
            status=status.HTTP_200_OK,
        )


class JobApplicationDashboardAPIView(generics.GenericAPIView):
    serializer_class = JobApplicationDashboardSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    @extend_schema(responses=JobApplicationDashboardSerializer)
    def get(self, request, *args, **kwargs):
        applications = JobApplication.objects.filter(user=request.user)

        total_applications = applications.count()
        accepted_applications = applications.filter(is_accepted=True).count()
        acceptance_rate = (
            round(accepted_applications / total_applications * 100, 2)
            if total_applications
            else None
        )

        interviews = InterviewStage.objects.filter(application__user=request.user)
        total_interviews = interviews.count()
        upcoming_interviews = interviews.filter(
            scheduled_at__gte=timezone.now()
        ).count()

        offers = Offer.objects.filter(application__user=request.user)
        total_offers = offers.count()
        upcoming_offers = offers.filter(
            start_date__gte=timezone.localtime(timezone.now()).date()
        ).count()

        applications_by_status = [
            {"status": row["status__title"], "count": row["count"]}
            for row in applications.values("status__title")
            .annotate(count=Count("id"))
            .order_by(F("count").desc())
        ]

        data = {
            "total_applications": total_applications,
            "accepted_applications": accepted_applications,
            "acceptance_rate": acceptance_rate,
            "total_interviews": total_interviews,
            "upcoming_interviews": upcoming_interviews,
            "total_offers": total_offers,
            "upcoming_offers": upcoming_offers,
            "applications_by_status": applications_by_status,
        }

        serializer = self.get_serializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
