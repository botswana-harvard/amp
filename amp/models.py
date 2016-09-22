from django.db import models
from django.utils import timezone
from edc_base.model.models.base_uuid_model import BaseUuidModel
from edc_consent.models.base_consent import BaseConsent, ConsentManager
from edc_consent.models.fields.bw.identity_fields_mixin import IdentityFieldsMixin
from edc_consent.models.fields.review_fields_mixin import ReviewFieldsMixin
from edc_consent.models.fields.personal_fields_mixin import PersonalFieldsMixin
from edc_consent.models.fields.citizen_fields_mixin import CitizenFieldsMixin
from edc_consent.models.fields.vulnerability_fields_mixin import VulnerabilityFieldsMixin
from simple_history.models import HistoricalRecords
from edc_constants.constants import MALE, FEMALE
from edc_visit_tracking.models.visit_model_mixin import VisitModelMixin
from edc_consent.models.requires_consent_mixin import RequiresConsentMixin
from edc_appointment.model_mixins import AppointmentModelMixin, CreateAppointmentsMixin


class AlreadyAllocatedError(Exception):
    pass


class SubjectIdentifier(BaseUuidModel):

    subject_identifier = models.CharField(
        max_length=12,
        unique=True
    )

    allocated_datetime = models.DateTimeField(
        null=True
    )

    def save(self, *args, **kwargs):
        if self.id and self.allocated_datetime:
            raise AlreadyAllocatedError('Identifier already allocated on {}. Got {}.'.format(
                self.allocated_datetime, self.subject_identifier))
        elif self.id:
            self.allocated_datetime = timezone.now()
        super(SubjectIdentifier, self).save(*args, **kwargs)

    class Meta:
        app_label = 'amp'
        ordering = ('subject_identifier', )


class ScreeningConsent(BaseConsent, IdentityFieldsMixin, ReviewFieldsMixin,
                       PersonalFieldsMixin, CitizenFieldsMixin, VulnerabilityFieldsMixin, BaseUuidModel):
    MIN_AGE_OF_CONSENT = 18
    MAX_AGE_OF_CONSENT = 99
    AGE_IS_ADULT = 18
    GENDER_OF_CONSENT = [MALE, FEMALE]
    SUBJECT_TYPES = ['subject']

    interviewed = models.BooleanField(default=False, editable=False)

    idi = models.BooleanField(default=False, editable=False)

    fgd = models.BooleanField(default=False, editable=False)

    history = HistoricalRecords()

    consent = ConsentManager()

    objects = models.Manager()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name, self.identity, self.subject_identifier)

    def natural_key(self):
        return (self.subject_identifier, )

    def save(self, *args, **kwargs):
        if not self.id:
            self.subject_identifier = SubjectIdentifier(site_code='99').get_identifier()
        super(ScreeningConsent, self).save(*args, **kwargs)

    class Meta:
        app_label = 'amp'
        get_latest_by = 'consent_datetime'
        unique_together = (('first_name', 'dob', 'initials', 'version'), )
        ordering = ('created', )


class StudyConsent(BaseConsent, IdentityFieldsMixin, ReviewFieldsMixin,
                   PersonalFieldsMixin, CitizenFieldsMixin, VulnerabilityFieldsMixin, BaseUuidModel):
    MIN_AGE_OF_CONSENT = 18
    MAX_AGE_OF_CONSENT = 99
    AGE_IS_ADULT = 18
    GENDER_OF_CONSENT = [MALE, FEMALE]
    SUBJECT_TYPES = ['subject']

    interviewed = models.BooleanField(default=False, editable=False)

    idi = models.BooleanField(default=False, editable=False)

    fgd = models.BooleanField(default=False, editable=False)

    history = HistoricalRecords()

    consent = ConsentManager()

    objects = models.Manager()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name, self.identity, self.subject_identifier)

    def natural_key(self):
        return (self.subject_identifier, )

    def save(self, *args, **kwargs):
        if not self.id:
            self.subject_identifier = SubjectIdentifier(site_code='99').get_identifier()
        super(ScreeningConsent, self).save(*args, **kwargs)

    class Meta:
        app_label = 'amp'
        get_latest_by = 'consent_datetime'
        unique_together = (('first_name', 'dob', 'initials', 'version'), )
        ordering = ('created', )


class SubjectVisit(VisitModelMixin, CreatesMetadataModelMixin, RequiresConsentMixin,
                   PreviousVisitModelMixin, BaseUuidModel):

    appointment = models.OneToOneField(Appointment)

    class Meta:
        consent_model = 'amp.studyconsent'
        app_label = 'amp'


class Appointment(AppointmentModelMixin, RequiresConsentMixin, BaseUuidModel):

    class Meta:
        consent_model = 'amp.studyconsent'
        app_label = 'amp'
