from django.core.urlresolvers import reverse
from django.db import models

from django.utils import timezone

from simple_history.models import HistoricalRecords

from edc_base.model.models.base_uuid_model import BaseUuidModel
from edc_base.utils import formatted_age

from edc_consent.field_mixins import ReviewFieldsMixin, PersonalFieldsMixin, CitizenFieldsMixin, VulnerabilityFieldsMixin
from edc_consent.field_mixins.bw.identity_fields_mixin import IdentityFieldsMixin
from edc_consent.managers import ConsentManager
from edc_consent.model_mixins import ConsentModelMixin
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin

from .subject_identifier import SubjectIdentifier
from .enrollment import Enrollment
from django.core.exceptions import ValidationError


class AlreadyAllocatedError(Exception):
    pass


class ScreeningConsent(ConsentModelMixin, UpdatesOrCreatesRegistrationModelMixin, IdentityFieldsMixin, ReviewFieldsMixin,
                       PersonalFieldsMixin, CitizenFieldsMixin, VulnerabilityFieldsMixin,
                       BaseUuidModel):

    objects = models.Manager()

    history = HistoricalRecords()

    consent = ConsentManager()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name, self.identity, self.subject_identifier)

    def save(self, *args, **kwargs):
        if not self.id:
            if self.subject_identifier:
                if self.__class__.objects.filter(subject_identifier=self.subject_identifier).exists():
                    raise ValidationError(
                        'Identifier already in use. Got {}'.format(self.subject_identifier))
                try:
                    SubjectIdentifier.objects.get(subject_identifier=self.subject_identifier)
                except SubjectIdentifier.DoesNotExist:
                    raise ValidationError(
                        'Invalid subject identifier. Got {}'.format(
                            self.subject_identifier))
            else:
                # SubjectIdentifier updated in the post_save
                self.subject_identifier = SubjectIdentifier.objects.filter(
                    allocated_datetime__isnull=True).order_by('created').first()
        super(ScreeningConsent, self).save(*args, **kwargs)

    def natural_key(self):
        return (self.subject_identifier, )

    def create_enrollment(self):
        try:
            Enrollment.objects.get(subject_identifier=self.subject_identifier)
        except Enrollment.DoesNotExist:
            Enrollment.objects.create(
                subject_identifier=self.subject_identifier,
                is_eligible=False
            )

    def age(self):
        return formatted_age(self.dob)

    def dashboard(self):
        """Returns a hyperink for the Admin page."""
        url = reverse(
            'subject_dashboard_url',
            kwargs={
                'subject_identifier': self.subject_identifier
            })
        ret = """<a href="{url}" >dashboard</a>""".format(url=url)
        return ret
    dashboard.allow_tags = True

    class Meta:
        app_label = 'amp'
        get_latest_by = 'consent_datetime'
        unique_together = (
            ('first_name', 'dob', 'initials', 'version'),
            ('subject_identifier', ))
        ordering = ('created', )
