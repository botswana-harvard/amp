from datetime import datetime
from django.test.testcases import TestCase

from .factories import ScreeningConsentFactory
from .models import ScreeningConsent, SubjectIdentifier, Appointment, Enrollment, RegisteredSubject


class TestScreeningConsentIdentifierAllocation(TestCase):

    def setUp(self):
        for identifier in ['1001243-1', '1001243-2', '1001243-3', '1001243-4', '1001243-5', '1001243-6']:
            SubjectIdentifier.objects.create(
                subject_identifier=identifier
            )

    def test_identifiers(self):
        self.assertEqual(6, SubjectIdentifier.objects.all().count())

    def test_allocate_identifier(self):

        ScreeningConsentFactory()
        ScreeningConsentFactory()
        self.assertEqual(RegisteredSubject.objects.filter(subject_identifier='1001243-1').count(), 1)

        self.assertEqual(ScreeningConsent.objects.filter(subject_identifier='1001243-1').count(), 1)

    def test_allocate_identifier_on_resave(self):

        ScreeningConsentFactory()

        self.assertEqual(ScreeningConsent.objects.filter(subject_identifier='1001243-1').count(), 1)

        screeningconsent = ScreeningConsent.objects.get(subject_identifier='1001243-1')
        screeningconsent.save()

        self.assertEqual(SubjectIdentifier.objects.filter(allocated_datetime=None).count(), 5)

    def test_allocate_identifier2(self):

        ScreeningConsentFactory()  # allocate the first identifier

        self.assertEqual(ScreeningConsent.objects.filter(subject_identifier='1001243-1').count(), 1)

        ScreeningConsentFactory()  # allocate the second identifier

        self.assertEqual(ScreeningConsent.objects.filter(subject_identifier='1001243-2').count(), 1)

    def test_allocate_identifier2_resave(self):

        ScreeningConsentFactory()  # allocate the first identifier

        screeningconsent = ScreeningConsent.objects.get(subject_identifier='1001243-1')
        screeningconsent.save()

        ScreeningConsentFactory()  # allocate the second identifier

        screeningconsent = ScreeningConsent.objects.get(subject_identifier='1001243-2')
        screeningconsent.save()

        self.assertEqual(SubjectIdentifier.objects.filter(allocated_datetime=None).count(), 4)

    def test_allocate_identifier_all(self):

        for _ in range(5):
            ScreeningConsentFactory()

        for identifier in ['1001243-1', '1001243-2', '1001243-3', '1001243-4', '1001243-5']:
            self.assertEqual(ScreeningConsent.objects.filter(subject_identifier=identifier).count(), 1)

    def test_create_enrollment_post_save(self):
        screening = ScreeningConsent.objects.create(
            consent_datetime=datetime.today(),
            identity='317918515',
            is_literate='Yes',
            confirm_identity='317918515',
            first_name='TESTA',
            last_name='TESTA',
        )
        self.assertEqual(Enrollment.objects.filter(subject_identifier=screening.subject_identifier).count(), 1)

    def test_create_enrollment_post_save_appointments(self):
        ScreeningConsentFactory()
        self.assertEqual(Appointment.objects.all().count(), 25)
