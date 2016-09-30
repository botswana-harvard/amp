from edc_base.model.models.base_uuid_model import BaseUuidModel

from edc_consent.model_mixins import RequiresConsentMixin
from edc_appointment.model_mixins import AppointmentModelMixin


class Appointment(AppointmentModelMixin, RequiresConsentMixin, BaseUuidModel):

    class Meta:
        consent_model = 'amp.screeningconsent'
        app_label = 'amp'
