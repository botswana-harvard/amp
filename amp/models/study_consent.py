from django.db import models
from edc_base.model.models.base_uuid_model import BaseUuidModel
from edc_consent.models.base_consent import BaseConsent, ConsentManager
from edc_consent.models.fields.bw.identity_fields_mixin import IdentityFieldsMixin
from edc_consent.models.fields.review_fields_mixin import ReviewFieldsMixin
from edc_consent.models.fields.personal_fields_mixin import PersonalFieldsMixin
from edc_consent.models.fields.citizen_fields_mixin import CitizenFieldsMixin
from edc_consent.models.fields.vulnerability_fields_mixin import VulnerabilityFieldsMixin
from simple_history.models import HistoricalRecords
from edc_constants.constants import MALE, FEMALE

from .subject_identifier import SubjectIdentifier


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
        super(StudyConsent, self).save(*args, **kwargs)

    class Meta:
        app_label = 'amp'
        get_latest_by = 'consent_datetime'
        unique_together = (('first_name', 'dob', 'initials', 'version'), )
        ordering = ('created', )
