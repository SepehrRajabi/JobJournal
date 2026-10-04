from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.test import TestCase

from .models import ClientContactInfo


class LinkedInValidatorTests(TestCase):
    def setUp(self):
        self.validator = next(
            validator
            for validator in ClientContactInfo._meta.get_field("linkedin").validators
            if type(validator) is RegexValidator
        )

    def test_accepts_standard_profile_url(self):
        self.validator("https://www.linkedin.com/in/someone")

    def test_accepts_country_subdomain(self):
        self.validator("https://de.linkedin.com/company/example")

    def test_accepts_bare_domain_without_path(self):
        self.validator("https://linkedin.com")

    def test_is_case_insensitive(self):
        self.validator("https://WWW.LINKEDIN.COM/in/someone")

    def test_rejects_domain_suffix_bypass(self):
        with self.assertRaises(ValidationError):
            self.validator("https://linkedin.com.evil.com/in/someone")

    def test_rejects_unrelated_domain(self):
        with self.assertRaises(ValidationError):
            self.validator("https://notlinkedin.com")
