from django.utils import timezone

from django.test.testcases import TestCase

from model_mommy import mommy

from edc_constants.constants import FEMALE

from .models import ScreeningConsent, SubjectIdentifier, Appointment, Enrollment, RegisteredSubject
from .forms import ScreeningConsentForm


class TestScreeningConsentIdentifierAllocation(TestCase):

    def setUp(self):
        for identifier in ['1001243-1', '1001243-2', '1001243-3', '1001243-4', '1001243-5', '1001243-6']:
            SubjectIdentifier.objects.create(
                subject_identifier=identifier
            )

    def test_identifiers(self):
        self.assertEqual(6, SubjectIdentifier.objects.all().count())

    def test_allocate_identifier(self):

        mommy.make(ScreeningConsent, identity='111121118', confirm_identity='111121118')
        mommy.make(ScreeningConsent, identity='111121117', confirm_identity='111121117')
        self.assertEqual(RegisteredSubject.objects.filter(subject_identifier='1001243-1').count(), 1)

        self.assertEqual(ScreeningConsent.objects.filter(subject_identifier='1001243-1').count(), 1)

    def test_allocate_identifier_on_resave(self):

        mommy.make(ScreeningConsent, identity='111121116', confirm_identity='111121116')

        self.assertEqual(ScreeningConsent.objects.filter(subject_identifier='1001243-1').count(), 1)

        screeningconsent = ScreeningConsent.objects.get(subject_identifier='1001243-1')
        screeningconsent.save()

        self.assertEqual(SubjectIdentifier.objects.filter(allocated_datetime=None).count(), 5)

    def test_allocate_identifier2(self):

        mommy.make(ScreeningConsent, identity='111121115', confirm_identity='111121115')

        self.assertEqual(ScreeningConsent.objects.filter(subject_identifier='1001243-1').count(), 1)

        mommy.make(ScreeningConsent, identity='111121114', confirm_identity='111121114')

        self.assertEqual(ScreeningConsent.objects.filter(subject_identifier='1001243-2').count(), 1)

    def test_allocate_identifier2_resave(self):

        mommy.make(ScreeningConsent, identity='111121113', confirm_identity='111121113')

        screeningconsent = ScreeningConsent.objects.get(subject_identifier='1001243-1')
        screeningconsent.save()

        mommy.make(ScreeningConsent, identity='111121112', confirm_identity='111121112')

        screeningconsent = ScreeningConsent.objects.get(subject_identifier='1001243-2')
        screeningconsent.save()

        self.assertEqual(SubjectIdentifier.objects.filter(allocated_datetime=None).count(), 4)


class TestEnrollmentCreation(TestCase):

    def setUp(self):
        for identifier in ['1001567-1', '1009997-1']:
            SubjectIdentifier.objects.create(
                subject_identifier=identifier
            )

    def test_create_enrollment_post_save(self):
        screening = ScreeningConsent.objects.create(
            consent_datetime=timezone.now(),
            identity='317928515',
            is_literate='Yes',
            confirm_identity='317928515',
            first_name='TESTA',
            last_name='TESTA',
        )
        self.assertEqual(Enrollment.objects.filter(subject_identifier=screening.subject_identifier).count(), 1)

    def test_create_enrollment_post_save_appointments(self):
        mommy.make(ScreeningConsent, identity='317928919', confirm_identity='317928919')
        self.assertEqual(Appointment.objects.all().count(), 25)


class TestConsentScreeningForm(TestCase):

    def setUp(self):

        self.data = {
            'initials': 'LB',
            'dob': timezone.datetime(1990, 12, 16).date(),
            'identity': '111121345',
            'identity_type': 'omang',
            'is_literate': 'Yes',
            'confirm_identity': '111121345',
            'first_name': 'LAME',
            'gender': FEMALE,
            'consent_datetime': timezone.now(),
            'last_name': 'BAME',
            'subject_identifier': '1223423-23'}
        self.subject_identifier = '1223423-23'

        for identifier in ['123143-34', '123143-32', '123143-31', '123143-33']:
            SubjectIdentifier.objects.create(
                subject_identifier=identifier
            )

    def test_wrong_subject_identifier(self):
        """Test to verify that validation for initial visit date works"""
        form = ScreeningConsentForm(data=self.data)
        errors = ''.join(form.errors.get('__all__'))
        self.assertIn(
            'The Subject Identifier entered does not exist in the list of identifiers provided. Got {}'.format(
                self.subject_identifier), errors)
