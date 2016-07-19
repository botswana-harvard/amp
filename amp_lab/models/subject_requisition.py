from django.db import models

# from edc_base.audit_trail import AuditTrail
from edc_base.model.models.base_uuid_model import BaseUuidModel
from edc_export.models import ExportTrackingFieldsMixin
from edc_meta_data.managers import RequisitionMetaDataManager
from edc_visit_tracking.models import CrfModelManager, CrfModelMixin
from lab_requisition.models import RequisitionModelMixin

#from td_infant.models import InfantVisit

from .aliquot import Aliquot
from .aliquot_type import AliquotType
from .packing_list import PackingList
from .panel import Panel


class SubjectRequisitionManager(CrfModelManager):

    def get_by_natural_key(self, requisition_identifier):
        return self.get(requisition_identifier=requisition_identifier)


class SubjectRequisition(CrfModelMixin, RequisitionModelMixin, BaseUuidModel):

    aliquot_model = Aliquot

    #subject_visit = models.ForeignKey(SubjectVisit)

    packing_list = models.ForeignKey(PackingList, null=True, blank=True)

    aliquot_type = models.ForeignKey(AliquotType)

    panel = models.ForeignKey(Panel)

    objects = SubjectRequisitionManager()

    #entry_meta_data_manager = RequisitionMetaDataManager(InfantVisit)

    def get_visit(self):
        return self.infant_visit

    class Meta:
        app_label = 'amp_lab'
        verbose_name = 'Subject Requisition'
        verbose_name_plural = 'Subject Laboratory Requisition'
        #unique_together = ('infant_visit', 'panel', 'is_drawn')
