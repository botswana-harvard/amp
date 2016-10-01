from datetime import datetime
from django.test.testcases import TestCase

from amp.models import ScreeningConsent, SubjectIdentifier, Appointment
from amp.factories import ScreeningConsentFactory, EnrollmentFactory
from amp.models.enrollment import Enrollment
from amp.models.registered_subject import RegisteredSubject
from amp.models.subject_visit import SubjectVisit
from amp.models.requisition_meta_data import RequisitionMetadata, CrfMetadata


class TestScreeningConsentIdentifierAllocation(TestCase):

    def setUp(self):
        for identifier in ['1001243-1', '1001243-2', '1001243-3', '1001243-4', '1001243-5']:
            SubjectIdentifier.objects.create(
                subject_identifier=identifier
            )

    def test_identifiers(self):
        self.assertEqual(5, SubjectIdentifier.objects.all().count())

    def test_allocate_identifier(self):

        ScreeningConsentFactory()
        self.assertEqual(RegisteredSubject.objects.filter(subject_identifier='1001243-1').count(), 1)

        self.assertEqual(ScreeningConsent.objects.filter(subject_identifier='1001243-1').count(), 1)

    def test_allocate_identifier_on_resave(self):

        ScreeningConsentFactory()

        self.assertEqual(ScreeningConsent.objects.filter(subject_identifier='1001243-1').count(), 1)

        screeningconsent = ScreeningConsent.objects.get(subject_identifier='1001243-1')
        screeningconsent.save()

        self.assertEqual(SubjectIdentifier.objects.filter(allocated_datetime=None).count(), 4)

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

        self.assertEqual(SubjectIdentifier.objects.filter(allocated_datetime=None).count(), 3)

    def test_allocate_identifier_all(self):

        for _ in range(5):
            ScreeningConsentFactory()

        for identifier in ['1001243-1', '1001243-2', '1001243-3', '1001243-4', '1001243-5']:
            self.assertEqual(ScreeningConsent.objects.filter(subject_identifier=identifier).count(), 1)

    def test_create_enrollment_post_save(self):
        screening = ScreeningConsentFactory()
        EnrollmentFactory(subject_identifier=screening.subject_identifier)
        self.assertEqual(Enrollment.objects.all().count(), 1)

    def test_create_enrollment_post_save_appointments(self):
        screening = ScreeningConsentFactory()
        EnrollmentFactory(subject_identifier=screening.subject_identifier)

        self.assertEqual(Appointment.objects.all().count(), 1)

    def test_create_subject_visit_and_metadata_at_enrollment(self):
        screening = ScreeningConsentFactory()
        EnrollmentFactory(subject_identifier=screening.subject_identifier)
        appointment = Appointment.objects.first()

        SubjectVisit.objects.create(
            appointment=appointment,
            report_datetime=datetime.today(),
            reason='scheduled',
        )
        self.assertEqual(CrfMetadata.objects.all().count(), 0)
        self.assertEqual(RequisitionMetadata.objects.all().count(), 2)
