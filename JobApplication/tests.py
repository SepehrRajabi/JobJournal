from django.test import TestCase

from Asset.models import AssetExtension, AssetGroup, AssetType, Document, VersionedDocument
from User.models import User

from .models import JobApplication
from .serializers import JobApplicationCreateSerializer
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


class JobApplicationResumeFreezeTests(TestCase):
    """
    resume/cover_letter freeze to whichever Document was the AssetGroup's
    get_latest_version() at submission time, rather than staying a live
    pointer that would silently drift if a newer version is uploaded
    afterwards.
    """

    def setUp(self):
        self.user = User.objects.create_user(
            first_name="Test",
            last_name="User",
            email="test@example.com",
            password="password123",
        )
        extension = AssetExtension.objects.create(extension="pdf")
        self.asset_type = AssetType.objects.create(name="Resume")
        self.asset_type.supported_extensions.add(extension)
        self.cv_group = AssetGroup.objects.create(name="CV")

    def _link_new_version(self, name):
        document = Document.objects.create(
            title=name, user=self.user, asset_type=self.asset_type, file=name
        )
        VersionedDocument.objects.create(asset_group=self.cv_group, document=document)
        return document

    def _create_application(self, **overrides):
        data = {
            "user": str(self.user.pk),
            "title": "Backend Engineer",
            "location": "Remote",
            "employment_type": "Full-time",
            "work_mode": "Remote",
            "source": "LinkedIn",
            "job_url": "https://example.com/job/1",
            "resume": str(self.cv_group.pk),
        }
        data.update(overrides)
        serializer = JobApplicationCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.save()

    def test_resume_freezes_to_the_group_latest_version_at_creation(self):
        v1 = self._link_new_version("resume-v1.pdf")

        application = self._create_application()

        self.assertEqual(application.resume, v1)

    def test_resume_does_not_drift_when_a_newer_version_is_uploaded_later(self):
        v1 = self._link_new_version("resume-v1.pdf")
        application = self._create_application()
        self._link_new_version("resume-v2.pdf")

        application.refresh_from_db()

        self.assertEqual(application.resume, v1)
        self.assertEqual(self.cv_group.get_latest_version().title, "resume-v2.pdf")

    def test_resume_rejects_a_group_with_no_versions(self):
        empty_group = AssetGroup.objects.create(name="Empty")
        data = {
            "user": str(self.user.pk),
            "title": "Backend Engineer",
            "location": "Remote",
            "employment_type": "Full-time",
            "work_mode": "Remote",
            "source": "LinkedIn",
            "job_url": "https://example.com/job/1",
            "resume": str(empty_group.pk),
        }
        serializer = JobApplicationCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("resume", serializer.errors)
