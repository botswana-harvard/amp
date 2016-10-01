from django.db import models

from amp.models import Appointment
from amp.models import RegisteredSubject

from edc_base.model.models.base_uuid_model import BaseUuidModel

from edc_metadata.model_mixins import (
    CrfMetadataModelMixin, RequisitionMetadataModelMixin)


class RequisitionMetadata(RequisitionMetadataModelMixin, BaseUuidModel):

    registered_subject = models.ForeignKey(RegisteredSubject)

    appointment = models.ForeignKey(Appointment, related_name='+')

    class Meta(RequisitionMetadataModelMixin.Meta):
        app_label = 'amp'


class CrfMetadata(CrfMetadataModelMixin, BaseUuidModel):

    registered_subject = models.ForeignKey(RegisteredSubject)

    appointment = models.ForeignKey(Appointment, related_name='+')

    class Meta(CrfMetadataModelMixin.Meta):
        app_label = 'amp'
