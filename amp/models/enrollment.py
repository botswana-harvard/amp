from edc_appointment.model_mixins import CreateAppointmentsMixin
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_consent.model_mixins import RequiresConsentMixin
from edc_visit_schedule.model_mixins import EnrollmentModelMixin


class Enrollment(EnrollmentModelMixin, CreateAppointmentsMixin, RequiresConsentMixin, BaseUuidModel):

    class Meta(EnrollmentModelMixin.Meta):
        visit_schedule_name = 'visit_schedule1.schedule1'
        consent_model = 'amp.screeningconsent'
        app_label = 'amp'
