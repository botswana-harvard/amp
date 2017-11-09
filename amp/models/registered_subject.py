from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_registration.model_mixins import RegisteredSubjectModelMixin


class RegisteredSubject(RegisteredSubjectModelMixin, BaseUuidModel):

    class Meta:
        app_label = 'amp'
