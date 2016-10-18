from django.db import models
from django.utils import timezone

from edc_appointment.model_mixins import CreateAppointmentsMixin
from edc_base.model.models.base_uuid_model import BaseUuidModel
from edc_consent.model_mixins import RequiresConsentMixin
from edc_registration.model_mixins import RegisteredSubjectMixin


class Enrollment(CreateAppointmentsMixin, RegisteredSubjectMixin, RequiresConsentMixin, BaseUuidModel):

    report_datetime = models.DateTimeField(default=timezone.now)

    is_eligible = models.BooleanField(default=True)

    class Meta:
        visit_schedule_name = 'subject_visit_schedule'
        consent_model = 'amp.screeningconsent'
        app_label = 'amp'
