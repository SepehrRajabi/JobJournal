from datetime import timedelta

from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from django.utils import timezone

from JobApplication.models import InterviewStage
from Notification.models import Notification
from User.models import User


class Command(BaseCommand):
    help = "Send reminders for interviews scheduled within an upcoming time window."

    def add_arguments(self, parser):
        parser.add_argument(
            "--hours",
            type=int,
            default=24,
            help="Remind for interviews scheduled within this many hours from now (default: 24).",
        )

    def handle(self, *args, **options):
        now = timezone.now()
        window_end = now + timedelta(hours=options["hours"])

        stages = list(
            InterviewStage.objects.select_related(
                "application", "application__user"
            ).filter(
                application__isnull=False,
                scheduled_at__gte=now,
                scheduled_at__lte=window_end,
            )
        )

        content_type = ContentType.objects.get_for_model(InterviewStage)
        already_reminded = set(
            Notification.objects.filter(
                action=Notification.ActionChoices.UPCOMING_INTERVIEW_REMINDER,
                object_type=content_type,
                object_id__in=[str(stage.pk) for stage in stages],
            ).values_list("object_id", flat=True)
        )

        sent = 0
        for stage in stages:
            if str(stage.pk) in already_reminded:
                continue

            notification = Notification.objects.create(
                subject=stage.application,
                object=stage,
                action=Notification.ActionChoices.UPCOMING_INTERVIEW_REMINDER,
                message=(
                    f"Upcoming interview for {stage.application.title}: "
                    f"{stage.title} on {timezone.localtime(stage.scheduled_at):%Y-%m-%d %H:%M}."
                ),
            )
            notification.dispatch_for_users(
                User.objects.filter(id=stage.application.user_id)
            )
            sent += 1

        self.stdout.write(f"Sent {sent} interview reminder(s).")
