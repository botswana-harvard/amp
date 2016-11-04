from django.db import models

from edc_base.model.models import BaseUuidModel
from edc_consent.model_mixins import RequiresConsentMixin

from edc_offstudy.model_mixins import OffStudyModelMixin

from edc_visit_tracking.model_mixins import CrfModelMixin
from .screening_consent import ScreeningConsent
from .subject_visit import SubjectVisit


class SubjectOffStudy(OffStudyModelMixin, CrfModelMixin,
                      RequiresConsentMixin, BaseUuidModel):

    """ A model completed by the user on the visit when the subject is taken off-study. """

    consent_model = ScreeningConsent

    maternal_visit = models.OneToOneField(SubjectVisit)

    class Meta:
        app_label = 'amp'
        verbose_name = "Subject Off Study"
