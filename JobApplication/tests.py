from django.test import TestCase

from User.models import User

from .models import JobApplication
from .utils import get_job_application_history


class JobApplicationHistoryTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name="Test",
            last_name="User",
            email="test@example.com",
            password="password123",
        )

    def test_get_job_application_history_ignores_initial_snapshot_without_previous_record(
        self,
    ):
        application = JobApplication.objects.create(
            user=self.user,
            title="Backend Engineer",
            location="Remote",
            employment_type="Full-time",
            work_mode="Remote",
            source="LinkedIn",
            job_url="https://example.com/job/1",
        )

        application.title = "Senior Backend Engineer"
        application.save()

        history = get_job_application_history(application)

        self.assertEqual(len(history), 1)
        self.assertEqual(history[0]["changes"]["title"]["old"], "Backend Engineer")
        self.assertEqual(
            history[0]["changes"]["title"]["new"], "Senior Backend Engineer"
        )
