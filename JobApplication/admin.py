from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import (
    InterviewResult,
    InterviewStage,
    InterviewStageStatus,
    InterviewStageType,
    JobApplication,
    JobApplicationStatus,
    Opportunity,
)


class OpportunityInAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    search_fields = ["title"]
    ordering = ["title"]


admin.site.register(Opportunity, OpportunityInAdmin)


class JobApplicationStatusInAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    search_fields = ["title"]
    ordering = ["title"]


admin.site.register(JobApplicationStatus, JobApplicationStatusInAdmin)


class InterviewStageStatusInAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    search_fields = ["title"]
    ordering = ["title"]


admin.site.register(InterviewStageStatus, InterviewStageStatusInAdmin)


class InterviewStageTypeInAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    search_fields = ["title"]
    ordering = ["title"]


admin.site.register(InterviewStageType, InterviewStageTypeInAdmin)


class InterviewResultInAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    search_fields = ["title"]
    ordering = ["title"]


admin.site.register(InterviewResult, InterviewResultInAdmin)


class InterviewStageInline(admin.TabularInline):
    model = InterviewStage
    extra = 0
    fields = [
        "stage_order",
        "title",
        "stage_type",
        "status",
        "scheduled_at",
        "completed_at",
        "duration_minutes",
        "result",
    ]
    autocomplete_fields = ["stage_type", "status", "result"]
    ordering = ["stage_order"]
    show_change_link = True


class JobApplicationInAdmin(SimpleHistoryAdmin):
    list_display = [
        "title",
        "user",
        "client",
        "status",
        "employment_type",
        "work_mode",
        "applied_at",
        "created_at",
    ]
    list_filter = [
        "status",
        "employment_type",
        "work_mode",
        "currency",
        ("applied_at", admin.DateFieldListFilter),
        ("created_at", admin.DateFieldListFilter),
    ]
    search_fields = [
        "title",
        "location",
        "source",
        "user__first_name",
        "user__last_name",
        "user__email",
        "client__name",
    ]

    readonly_fields = ["id", "created_at"]
    autocomplete_fields = [
        "user",
        "opportunity",
        "status",
        "resume",
        "cover_letter",
    ]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "id",
                    "user",
                    "title",
                    "status",
                ),
            },
        ),
        (
            "Company & Role",
            {
                "fields": (
                    "client",
                    "opportunity",
                    "location",
                    "employment_type",
                    "work_mode",
                ),
            },
        ),
        (
            "Compensation",
            {
                "fields": (
                    "salary_min",
                    "salary_max",
                    "currency",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Application Details",
            {
                "fields": (
                    "source",
                    "job_url",
                    "applied_at",
                    "deadline",
                    "tags",
                ),
            },
        ),
        (
            "Documents",
            {
                "fields": (
                    "resume",
                    "cover_letter",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Notes",
            {
                "fields": ("notes",),
            },
        ),
        (
            "Metadata",
            {
                "fields": ("created_at",),
                "classes": ("collapse",),
            },
        ),
    )
    inlines = [InterviewStageInline]
    date_hierarchy = "applied_at"
    list_select_related = ["user", "client", "status"]
    ordering = ["-created_at"]


admin.site.register(JobApplication, JobApplicationInAdmin)


class InterviewStageInAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "application",
        "stage_order",
        "stage_type",
        "status",
        "scheduled_at",
        "result",
    ]
    list_filter = [
        "stage_type",
        "status",
        "result",
        ("scheduled_at", admin.DateFieldListFilter),
    ]
    search_fields = [
        "title",
        "application__title",
        "application__user__email",
    ]
    autocomplete_fields = [
        "application",
        "stage_type",
        "status",
        "result",
    ]
    readonly_fields = ["id"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "id",
                    "application",
                    "stage_order",
                    "title",
                    "stage_type",
                    "status",
                    "result",
                ),
            },
        ),
        (
            "Schedule",
            {
                "fields": (
                    "scheduled_at",
                    "completed_at",
                    "duration_minutes",
                ),
            },
        ),
        (
            "Location & Links",
            {
                "fields": (
                    "meeting_link",
                    "location",
                ),
            },
        ),
        (
            "Notes",
            {
                "fields": ("notes",),
            },
        ),
    )
    list_select_related = [
        "application",
        "stage_type",
        "status",
        "result",
    ]
    ordering = ["application", "stage_order"]


admin.site.register(InterviewStage, InterviewStageInAdmin)
