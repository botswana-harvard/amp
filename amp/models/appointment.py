from edc_base.model.models.base_uuid_model import BaseUuidModel

from edc_consent.model_mixins import RequiresConsentMixin
from edc_appointment.model_mixins import AppointmentModelMixin


class Appointment(AppointmentModelMixin, RequiresConsentMixin, BaseUuidModel):

    class Meta:
        consent_model = 'amp.screeningconsent'
        app_label = 'amp'

    @property
    def str_pk(self):
        return str(self.pk)

    @property
    def subject_visit(self):
        from amp.models.subject_visit import SubjectVisit
        try:
            return SubjectVisit.objects.get(appointment=self)
        except SubjectVisit.DoesNotExist:
            return None
