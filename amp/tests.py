from django.test.testcases import TestCase
from amp.models import ScreeningConsent, SubjectIdentifier
from amp.factories import ScreeningConsentFactory


class TestScreeningConsentIdentifierAllocation(TestCase):

    def setUp(self):
        for identifier in ['1001243-1', '1001243-2', '1001243-3', '1001243-4', '1001243-5']:
            SubjectIdentifier.objects.create(
                subject_identifier=identifier
            )

    def test_allocate_identifier(self):

        ScreeningConsentFactory()

        self.assertEqual(ScreeningConsent.objects.filter(subject_identifier='1001243-1').count(), 1)

    def test_allocate_identifier2(self):

        ScreeningConsentFactory()  # allocate the first identifier

        self.assertEqual(ScreeningConsent.objects.filter(subject_identifier='1001243-1').count(), 1)

        ScreeningConsentFactory()  # allocate the second identifier

        self.assertEqual(ScreeningConsent.objects.filter(subject_identifier='1001243-2').count(), 1)

    def test_allocate_identifier_all(self):

        for _ in range(5):
            ScreeningConsentFactory()

        for identifier in ['1001243-1', '1001243-2', '1001243-3', '1001243-4', '1001243-5']:
            self.assertEqual(ScreeningConsent.objects.filter(subject_identifier=identifier).count(), 1)
