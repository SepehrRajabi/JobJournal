from uuid import uuid4

from django.conf import settings
from django.db import models
from simple_history.models import HistoricalRecords

from Asset.models import AssetGroup
from Client.models import Client


class Opportunity(models.Model):
    id = models.UUIDField(
        default=uuid4,
        editable=False,
        null=False,
        primary_key=True,
        unique=True,
        db_index=True,
    )
    title = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Opportunities"


class JobApplicationStatus(models.Model):
    id = models.UUIDField(
        default=uuid4,
        editable=False,
        null=False,
        primary_key=True,
        unique=True,
        db_index=True,
    )
    title = models.CharField(max_length=100, null=True, blank=True, unique=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Job Application Statuses"


class JobApplicationTag(models.Model):
    id = models.UUIDField(
        default=uuid4,
        editable=False,
        null=False,
        primary_key=True,
        unique=True,
        db_index=True,
    )
    title = models.CharField(max_length=100, null=True, blank=True, unique=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Job Application Tags"


class JobApplication(models.Model):
    id = models.UUIDField(
        default=uuid4,
        editable=False,
        null=False,
        primary_key=True,
        unique=True,
        db_index=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="job_applications",
    )

    client = models.ForeignKey(
        Client,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="job_applications",
    )
    opportunity = models.ForeignKey(
        Opportunity,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="job_applications",
    )

    title = models.CharField(max_length=255)

    location = models.CharField(max_length=255)

    employment_type = models.CharField(max_length=50)

    work_mode = models.CharField(max_length=30)

    salary_min = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )

    salary_max = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )

    currency = models.CharField(max_length=10, default="EUR")

    source = models.CharField(max_length=100)

    job_url = models.URLField(blank=True)

    status = models.ForeignKey(
        JobApplicationStatus,
        null=True,
        blank=True,
        related_name="job_applications",
        on_delete=models.SET_NULL,
    )

    applied_at = models.DateField(null=True, blank=True)

    deadline = models.DateField(null=True, blank=True)

    resume = models.ForeignKey(
        AssetGroup,
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    cover_letter = models.ForeignKey(
        AssetGroup,
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    tags = models.ManyToManyField(
        JobApplicationTag, blank=True, related_name="job_applications"
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords(m2m_fields=[tags])

    def __str__(self):
        return f"{self.title}"


class InterviewStageStatus(models.Model):
    id = models.UUIDField(
        default=uuid4,
        editable=False,
        null=False,
        primary_key=True,
        unique=True,
        db_index=True,
    )
    title = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Interview Stage Statuses"


class InterviewStageType(models.Model):
    id = models.UUIDField(
        default=uuid4,
        editable=False,
        null=False,
        primary_key=True,
        unique=True,
        db_index=True,
    )
    title = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class InterviewResult(models.Model):
    id = models.UUIDField(
        default=uuid4,
        editable=False,
        null=False,
        primary_key=True,
        unique=True,
        db_index=True,
    )
    title = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class InterviewStage(models.Model):
    id = models.UUIDField(
        default=uuid4,
        editable=False,
        null=False,
        primary_key=True,
        unique=True,
        db_index=True,
    )

    application = models.ForeignKey(
        JobApplication,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="interview_stages",
    )

    stage_order = models.PositiveIntegerField(default=0)

    stage_type = models.ForeignKey(
        InterviewStageType,
        null=True,
        blank=True,
        related_name="interview_stages",
        on_delete=models.SET_NULL,
    )

    title = models.CharField(max_length=255)

    status = models.ForeignKey(
        InterviewStageStatus,
        null=True,
        blank=True,
        related_name="interview_stages",
        on_delete=models.SET_NULL,
    )

    scheduled_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    duration_minutes = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    meeting_link = models.URLField(blank=True)

    location = models.CharField(
        max_length=255,
        blank=True,
    )

    result = models.ForeignKey(
        InterviewResult,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="interview_stages",
    )

    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.application.title} - {self.stage_order}"
