from django.db import models

from amp.models import Appointment
from amp.models import RegisteredSubject

from edc_base.model.models.base_uuid_model import BaseUuidModel

from edc_metadata.model_mixins import (
    CrfMetadataModelMixin, RequisitionMetadataModelMixin)
from amp.models.subject_requisition import SubjectRequisition


class RequisitionMetadata(RequisitionMetadataModelMixin, BaseUuidModel):

    registered_subject = models.ForeignKey(RegisteredSubject)

    appointment = models.ForeignKey(Appointment, related_name='+')

    class Meta(RequisitionMetadataModelMixin.Meta):
        app_label = 'amp'

    @property
    def subject_requisition(self):
        subject_requisition = None
        try:
            subject_requisition = SubjectRequisition.objects.get(subject_visit__appointment=self.appointment, panel_name=self.panel_name)
            print(subject_requisition.requisition_identifier, "subject_requisition i am in here")
        except SubjectRequisition.DoesNotExist:
            pass
        return subject_requisition


class CrfMetadata(CrfMetadataModelMixin, BaseUuidModel):

    registered_subject = models.ForeignKey(RegisteredSubject)

    appointment = models.ForeignKey(Appointment, related_name='+')

    class Meta(CrfMetadataModelMixin.Meta):
        app_label = 'amp'
