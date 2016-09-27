from django.db import models

# from edc_base.audit_trail import AuditTrail
from edc_base.model.models.base_uuid_model import BaseUuidModel

from edc_visit_tracking.model_mixins import CrfModelMixin
from edc_visit_tracking.managers import CrfModelManager
from edc_consent.model_mixins import RequiresConsentMixin

from edc_metadata.model_mixins import (
    CrfMetadataModelMixin, RequisitionMetadataModelMixin, CreatesMetadataModelMixin,
    UpdatesCrfMetadataModelMixin, UpdatesRequisitionMetadataModelMixin)

#from .aliquot import Aliquot
from .aliquot_type import AliquotType
from .packing_list import PackingList
from .panel import Panel
from edc_lab.requisition.model_mixins import RequisitionModelMixin
from edc_lab.requisition.managers import RequisitionManager
from amp.models.subject_visit import SubjectVisit


class SubjectRequisitionManager(CrfModelManager):

    def get_by_natural_key(self, requisition_identifier):
        return self.get(requisition_identifier=requisition_identifier)


class SubjectRequisition(CrfModelMixin, RequisitionModelMixin, RequiresConsentMixin,
                         UpdatesRequisitionMetadataModelMixin, BaseUuidModel):

#     aliquot_model = Aliquot

    subject_visit = models.ForeignKey(SubjectVisit)

    packing_list = models.ForeignKey(PackingList, null=True, blank=True)

#     aliquot_type = models.ForeignKey(AliquotType)

    panel = models.ForeignKey(Panel)

    objects = RequisitionManager()

    # entry_meta_data_manager = RequisitionMetaDataManager(SubjectVisit)

    def get_visit(self):
        return self.subject_visit

    class Meta:
        app_label = 'amp_lab'
        verbose_name = 'Subject Requisition'
        verbose_name_plural = 'Subject Laboratory Requisition'
        consent_model = 'amp.subjectconsent'
