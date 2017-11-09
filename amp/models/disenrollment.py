from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_consent.model_mixins import RequiresConsentMixin
from edc_visit_schedule.model_mixins import DisenrollmentModelMixin


class Disenrollment(DisenrollmentModelMixin, RequiresConsentMixin, BaseUuidModel):

    class Meta(DisenrollmentModelMixin.Meta):
        visit_schedule_name = 'visit_schedule1.schedule1'
        consent_model = 'amp.screeningconsent'
        app_label = 'amp'
