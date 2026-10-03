from datetime import timedelta

from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from django.utils import timezone

from JobApplication.models import Offer
from Notification.models import Notification
from User.models import User


class Command(BaseCommand):
    help = "Send reminders for offers whose decision deadline falls within an upcoming window."

    def add_arguments(self, parser):
        parser.add_argument(
            "--days",
            type=int,
            default=3,
            help="Remind for offers with a decision deadline within this many days from now (default: 3).",
        )

    def handle(self, *args, **options):
        today = timezone.localtime(timezone.now()).date()
        window_end = today + timedelta(days=options["days"])

        offers = list(
            Offer.objects.select_related("application", "application__user").filter(
                decision_deadline__gte=today,
                decision_deadline__lte=window_end,
            )
        )

        content_type = ContentType.objects.get_for_model(Offer)
        already_reminded = set(
            Notification.objects.filter(
                action=Notification.ActionChoices.UPCOMING_OFFER_DEADLINE_REMINDER,
                object_type=content_type,
                object_id__in=[str(offer.pk) for offer in offers],
            ).values_list("object_id", flat=True)
        )

        sent = 0
        for offer in offers:
            if str(offer.pk) in already_reminded:
                continue

            notification = Notification.objects.create(
                subject=offer.application,
                object=offer,
                action=Notification.ActionChoices.UPCOMING_OFFER_DEADLINE_REMINDER,
                message=(
                    f"Decision deadline for the offer on {offer.application.title} "
                    f"is {offer.decision_deadline:%Y-%m-%d}."
                ),
            )
            notification.dispatch_for_users(
                User.objects.filter(pk=offer.application.user_id)
            )
            sent += 1

        self.stdout.write(f"Sent {sent} offer deadline reminder(s).")
