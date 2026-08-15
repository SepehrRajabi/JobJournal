from django.contrib.auth import get_user_model
from django.db.models import F
from rest_framework import serializers
from rest_framework.fields import UUIDField

from User.serializers import UserDetailSerializer

from .models import (
    InterviewResult,
    InterviewStage,
    InterviewStageStatus,
    InterviewStageType,
    JobApplication,
    JobApplicationStatus,
    Opportunity,
)

User = get_user_model()


class OpportunityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ["id", "title"]


class OppurtunitiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ["id", "title"]


class OpportunityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ["title"]


class OpportunityUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ["title"]


class OpportunityDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ["id"]


class JobApplicationStatusDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplicationStatus
        fields = ["id", "title"]


class JobApplicationStatusesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplicationStatus
        fields = ["id", "title"]


class JobApplicationStatusCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplicationStatus
        fields = ["title"]


class JobApplicationStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplicationStatus
        fields = ["title"]


class JobApplicationStatusDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplicationStatus
        fields = ["id"]


class JobApplicationDetailSerializer(serializers.ModelSerializer):
    opportunity = OpportunityDetailSerializer(read_only=True)
    status = JobApplicationStatusDetailSerializer(read_only=True)
    user = UserDetailSerializer(read_only=True)
    interviews = serializers.SerializerMethodField(read_only=True)

    def get_interviews(self, obj):
        interviews = obj.interview_stages.order_by(F("stage_order").asc())
        return InterviewStagesListSerializer(interviews, many=True).data

    class Meta:
        model = JobApplication
        fields = [
            "id",
            "user",
            "client",
            "opportunity",
            "title",
            "location",
            "employment_type",
            "work_mode",
            "salary_min",
            "salary_max",
            "currency",
            "interviews",
            "source",
            "job_url",
            "status",
            "applied_at",
            "deadline",
            "resume",
            "cover_letter",
            "notes",
            "created_at",
        ]


class JobApplicationsListSerializer(serializers.ModelSerializer):
    opportunity = OpportunityDetailSerializer(read_only=True)
    status = JobApplicationStatusDetailSerializer(read_only=True)
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = JobApplication
        fields = [
            "id",
            "user",
            "client",
            "opportunity",
            "title",
            "location",
            "employment_type",
            "work_mode",
            "salary_min",
            "salary_max",
            "currency",
            "source",
            "job_url",
            "status",
            "applied_at",
            "deadline",
            "resume",
            "cover_letter",
            "notes",
            "created_at",
        ]


class JobApplicationCreateSerializer(serializers.ModelSerializer):
    opportunity = serializers.PrimaryKeyRelatedField(
        queryset=Opportunity.objects.all(),
        required=False,
        allow_null=True,
        pk_field=UUIDField(format="hex_verbose"),
    )
    status = serializers.PrimaryKeyRelatedField(
        queryset=JobApplicationStatus.objects.all(),
        required=False,
        allow_null=True,
        pk_field=UUIDField(format="hex_verbose"),
    )
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
        allow_null=True,
        pk_field=UUIDField(format="hex_verbose"),
    )

    class Meta:
        model = JobApplication
        fields = [
            "id",
            "user",
            "client",
            "opportunity",
            "title",
            "location",
            "employment_type",
            "work_mode",
            "salary_min",
            "salary_max",
            "currency",
            "source",
            "job_url",
            "status",
            "applied_at",
            "deadline",
            "resume",
            "cover_letter",
            "notes",
            "created_at",
        ]


class JobApplicationUpdateSerializer(serializers.ModelSerializer):
    opportunity = serializers.PrimaryKeyRelatedField(
        queryset=Opportunity.objects.all(),
        required=False,
        allow_null=True,
        pk_field=UUIDField(format="hex_verbose"),
    )
    status = serializers.PrimaryKeyRelatedField(
        queryset=JobApplicationStatus.objects.all(),
        required=False,
        allow_null=True,
        pk_field=UUIDField(format="hex_verbose"),
    )
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
        allow_null=True,
        pk_field=UUIDField(format="hex_verbose"),
    )

    class Meta:
        model = JobApplication
        fields = [
            "id",
            "user",
            "client",
            "opportunity",
            "title",
            "location",
            "employment_type",
            "work_mode",
            "salary_min",
            "salary_max",
            "currency",
            "source",
            "job_url",
            "status",
            "applied_at",
            "deadline",
            "resume",
            "cover_letter",
            "notes",
            "created_at",
        ]


class JobApplicationDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ["id"]


class InterviewStageStatusDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewStageStatus
        fields = ["id", "title"]


class InterviewStageStatusesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewStageStatus
        fields = ["id", "title"]


class InterviewStageStatusCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewStageStatus
        fields = ["id", "title"]


class InterviewStageStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewStageStatus
        fields = ["id", "title"]


class InterviewStageStatusDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewStageStatus
        fields = ["id"]


class InterviewStageTypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewStageType
        fields = ["id", "title"]


class InterviewStageTypesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewStageType
        fields = ["id", "title"]


class InterviewStageTypeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewStageType
        fields = ["id", "title"]


class InterviewStageTypeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewStageType
        fields = ["id", "title"]


class InterviewStageTypeDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewStageType
        fields = ["id"]


class InterviewResultDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewResult
        fields = ["id", "title"]


class InterviewResultsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewResult
        fields = ["id", "title"]


class InterviewResultCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewResult
        fields = ["id", "title"]


class InterviewResultUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewResult
        fields = ["id", "title"]


class InterviewResultDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewResult
        fields = ["id"]


class InterviewStageDetailSerializer(serializers.ModelSerializer):
    stage_type = InterviewStageTypeDetailSerializer(read_only=True)
    status = InterviewStageStatusDetailSerializer(read_only=True)
    result = InterviewResultDetailSerializer(read_only=True)

    class Meta:
        model = InterviewStage
        fields = [
            "id",
            "application",
            "stage_order",
            "stage_type",
            "title",
            "status",
            "scheduled_at",
            "completed_at",
            "duration_minutes",
            "meeting_link",
            "location",
            "result",
            "notes",
        ]


class InterviewStagesListSerializer(serializers.ModelSerializer):
    stage_type = InterviewStageTypeDetailSerializer(read_only=True)
    status = InterviewStageStatusDetailSerializer(read_only=True)
    result = InterviewResultDetailSerializer(read_only=True)

    class Meta:
        model = InterviewStage
        fields = [
            "id",
            "application",
            "stage_order",
            "stage_type",
            "title",
            "status",
            "scheduled_at",
            "completed_at",
            "duration_minutes",
            "meeting_link",
            "location",
            "result",
            "notes",
        ]


class InterviewStageCreateSerializer(serializers.ModelSerializer):
    stage_type = serializers.PrimaryKeyRelatedField(
        queryset=InterviewStageType.objects.all(),
        required=False,
        allow_null=True,
        pk_field=UUIDField(format="hex_verbose"),
    )
    status = serializers.PrimaryKeyRelatedField(
        queryset=InterviewStageStatus.objects.all(),
        required=False,
        allow_null=True,
        pk_field=UUIDField(format="hex_verbose"),
    )
    result = serializers.PrimaryKeyRelatedField(
        queryset=InterviewResult.objects.all(),
        required=False,
        allow_null=True,
        pk_field=UUIDField(format="hex_verbose"),
    )

    class Meta:
        model = InterviewStage
        fields = [
            "id",
            "application",
            "stage_order",
            "stage_type",
            "title",
            "status",
            "scheduled_at",
            "completed_at",
            "duration_minutes",
            "meeting_link",
            "location",
            "result",
            "notes",
        ]


class InterviewStageUpdateSerializer(serializers.ModelSerializer):
    stage_type = serializers.PrimaryKeyRelatedField(
        queryset=InterviewStageType.objects.all(),
        required=False,
        allow_null=True,
        pk_field=UUIDField(format="hex_verbose"),
    )
    status = serializers.PrimaryKeyRelatedField(
        queryset=InterviewStageStatus.objects.all(),
        required=False,
        allow_null=True,
        pk_field=UUIDField(format="hex_verbose"),
    )
    result = serializers.PrimaryKeyRelatedField(
        queryset=InterviewResult.objects.all(),
        required=False,
        allow_null=True,
        pk_field=UUIDField(format="hex_verbose"),
    )

    class Meta:
        model = InterviewStage
        fields = [
            "id",
            "application",
            "stage_order",
            "stage_type",
            "title",
            "status",
            "scheduled_at",
            "completed_at",
            "duration_minutes",
            "meeting_link",
            "location",
            "result",
            "notes",
        ]


class InterviewStageDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewStage
        fields = ["id"]
