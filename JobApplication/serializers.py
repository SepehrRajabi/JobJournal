from rest_framework import serializers

from .models import (
    InterviewResult,
    InterviewStage,
    InterviewStageStatus,
    InterviewStageType,
    JobApplication,
    JobApplicationStatus,
    Oppurtunity,
)


class OppurtunityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oppurtunity
        fields = ["id", "title"]


class OppurtunitiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oppurtunity
        fields = ["id", "title"]


class OppurtunityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oppurtunity
        fields = ["id", "title"]


class OppurtunityUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oppurtunity
        fields = ["id", "title"]


class OppurtunityDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oppurtunity
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
        fields = ["id", "title"]


class JobApplicationStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplicationStatus
        fields = ["id", "title"]


class JobApplicationStatusDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplicationStatus
        fields = ["id"]


class JobApplicationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = [
            "id",
            "user",
            "client",
            "oppurtunity",
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


class JobApplicationsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = [
            "id",
            "user",
            "client",
            "oppurtunity",
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
    class Meta:
        model = JobApplication
        fields = [
            "id",
            "user",
            "client",
            "oppurtunity",
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
    class Meta:
        model = JobApplication
        fields = [
            "id",
            "user",
            "client",
            "oppurtunity",
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
