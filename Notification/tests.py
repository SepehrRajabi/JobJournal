from datetime import timedelta

from django.core.management import call_command
from django.test import TestCase
from django.utils import timezone

from JobApplication.models import InterviewStage, JobApplication, Offer
from User.models import User

from .models import Notification, NotificationDispatch


class SendInterviewRemindersTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name="Test",
            last_name="User",
            email="test@example.com",
            password="password123",
        )
        self.application = JobApplication.objects.create(
            user=self.user,
            title="Backend Engineer",
            location="Remote",
            employment_type="Full-time",
            work_mode="Remote",
            source="LinkedIn",
            job_url="https://example.com/job/1",
        )

    def test_reminds_once_for_an_interview_within_the_window(self):
        InterviewStage.objects.create(
            application=self.application,
            title="Phone Screen",
            scheduled_at=timezone.now() + timedelta(hours=5),
        )

        call_command("send_interview_reminders", hours=24)

        self.assertEqual(
            Notification.objects.filter(
                action=Notification.ActionChoices.UPCOMING_INTERVIEW_REMINDER
            ).count(),
            1,
        )
        self.assertEqual(
            NotificationDispatch.objects.filter(recipient=self.user).count(), 1
        )

    def test_rerunning_does_not_create_duplicate_reminders(self):
        InterviewStage.objects.create(
            application=self.application,
            title="Phone Screen",
            scheduled_at=timezone.now() + timedelta(hours=5),
        )

        call_command("send_interview_reminders", hours=24)
        call_command("send_interview_reminders", hours=24)

        self.assertEqual(
            Notification.objects.filter(
                action=Notification.ActionChoices.UPCOMING_INTERVIEW_REMINDER
            ).count(),
            1,
        )

    def test_ignores_interviews_outside_the_window(self):
        InterviewStage.objects.create(
            application=self.application,
            title="Phone Screen",
            scheduled_at=timezone.now() + timedelta(hours=48),
        )

        call_command("send_interview_reminders", hours=24)

        self.assertEqual(
            Notification.objects.filter(
                action=Notification.ActionChoices.UPCOMING_INTERVIEW_REMINDER
            ).count(),
            0,
        )


class SendOfferDeadlineRemindersTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name="Test",
            last_name="User",
            email="test@example.com",
            password="password123",
        )
        self.application = JobApplication.objects.create(
            user=self.user,
            title="Backend Engineer",
            location="Remote",
            employment_type="Full-time",
            work_mode="Remote",
            source="LinkedIn",
            job_url="https://example.com/job/1",
            is_accepted=True,
        )

    def test_reminds_once_for_a_deadline_within_the_window(self):
        Offer.objects.create(
            application=self.application,
            decision_deadline=timezone.localtime(timezone.now()).date()
            + timedelta(days=2),
        )

        call_command("send_offer_deadline_reminders", days=3)

        self.assertEqual(
            Notification.objects.filter(
                action=Notification.ActionChoices.UPCOMING_OFFER_DEADLINE_REMINDER
            ).count(),
            1,
        )
        self.assertEqual(
            NotificationDispatch.objects.filter(recipient=self.user).count(), 1
        )

    def test_rerunning_does_not_create_duplicate_reminders(self):
        Offer.objects.create(
            application=self.application,
            decision_deadline=timezone.localtime(timezone.now()).date()
            + timedelta(days=2),
        )

        call_command("send_offer_deadline_reminders", days=3)
        call_command("send_offer_deadline_reminders", days=3)

        self.assertEqual(
            Notification.objects.filter(
                action=Notification.ActionChoices.UPCOMING_OFFER_DEADLINE_REMINDER
            ).count(),
            1,
        )

    def test_ignores_deadlines_outside_the_window(self):
        Offer.objects.create(
            application=self.application,
            decision_deadline=timezone.localtime(timezone.now()).date()
            + timedelta(days=10),
        )

        call_command("send_offer_deadline_reminders", days=3)

        self.assertEqual(
            Notification.objects.filter(
                action=Notification.ActionChoices.UPCOMING_OFFER_DEADLINE_REMINDER
            ).count(),
            0,
        )
