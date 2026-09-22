from django.test import TestCase

from User.models import User

from .models import AssetExtension, AssetGroup, AssetType, Document, VersionedDocument


class AssetGroupLatestVersionTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name="Test",
            last_name="User",
            email="test@example.com",
            password="password123",
        )
        self.extension = AssetExtension.objects.create(extension="pdf")
        self.asset_type = AssetType.objects.create(name="Resume")
        self.asset_type.supported_extensions.add(self.extension)

    def _create_document(self, name):
        # Assigning a plain string (rather than a File/ContentFile) leaves the
        # FieldFile already "committed", so no actual upload/storage call
        # happens here - tests stay independent of the storage backend.
        return Document.objects.create(
            title=name, user=self.user, asset_type=self.asset_type, file=name
        )

    def test_latest_version_returns_most_recently_linked_document(self):
        group = AssetGroup.objects.create(name="CV")
        older = self._create_document("resume-v1.pdf")
        newer = self._create_document("resume-v2.pdf")

        VersionedDocument.objects.create(asset_group=group, document=older)
        VersionedDocument.objects.create(asset_group=group, document=newer)

        self.assertEqual(group.latest_version, newer)

    def test_latest_version_reflects_newly_linked_document(self):
        group = AssetGroup.objects.create(name="CV")
        first = self._create_document("resume-v1.pdf")
        VersionedDocument.objects.create(asset_group=group, document=first)
        self.assertEqual(group.latest_version, first)

        second = self._create_document("resume-v2.pdf")
        VersionedDocument.objects.create(asset_group=group, document=second)
        self.assertEqual(group.latest_version, second)

    def test_latest_version_returns_none_for_empty_group(self):
        group = AssetGroup.objects.create(name="Empty")
        self.assertIsNone(group.latest_version)
