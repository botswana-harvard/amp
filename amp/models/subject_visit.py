from django.db import models

from edc_base.model.models import BaseUuidModel
from edc_consent.model_mixins import RequiresConsentMixin
from edc_metadata.model_mixins import CreatesMetadataModelMixin
from edc_visit_tracking.model_mixins import VisitModelMixin, PreviousVisitModelMixin


from .appointment import Appointment
from amp.models.registered_subject import RegisteredSubject


class SubjectVisit(VisitModelMixin, CreatesMetadataModelMixin, RequiresConsentMixin,
                   PreviousVisitModelMixin, BaseUuidModel):

    appointment = models.OneToOneField(Appointment)

    @property
    def metadata_query_options(self):
        options = super().metadata_query_options
        options.update({'appointment': self.appointment})
        options.update({'registered_subject': self.registered_subject})
        return options

    @property
    def registered_subject(self):
        try:
            registered_subject = RegisteredSubject.objects.get(subject_identifier=self.subject_identifier)
        except RegisteredSubject.DoesNotExist:
            return RegisteredSubject.objects.none()
        return registered_subject

    def metadata_run_rules(self, source_model=None):
        pass

    class Meta:
        consent_model = 'amp.screeningconsent'
        app_label = 'amp'
        verbose_name = 'Subject Visit'
