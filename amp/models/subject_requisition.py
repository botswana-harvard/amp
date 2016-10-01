from django.db import models

from edc_base.model.models.base_uuid_model import BaseUuidModel

from edc_visit_tracking.model_mixins import CrfModelMixin
from edc_visit_tracking.managers import CrfModelManager
from edc_consent.model_mixins import RequiresConsentMixin

from edc_metadata.model_mixins import UpdatesRequisitionMetadataModelMixin


from edc_lab.requisition.model_mixins import RequisitionModelMixin
from edc_lab.requisition.managers import RequisitionManager
from amp.models.subject_visit import SubjectVisit
from amp_lab.models.packing_list import PackingList
from amp_lab.models.panel import Panel


class SubjectRequisitionManager(CrfModelManager):

    def get_by_natural_key(self, requisition_identifier):
        return self.get(requisition_identifier=requisition_identifier)


class SubjectRequisition(CrfModelMixin, RequisitionModelMixin, RequiresConsentMixin,
                         UpdatesRequisitionMetadataModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    packing_list = models.ForeignKey(PackingList, null=True, blank=True)

    panel = models.ForeignKey(Panel)

    objects = RequisitionManager()

    #entry_meta_data_manager = CrfMetaDataManager(SubjectVisit)

    def get_visit(self):
        return self.subject_visit

    class Meta:
        app_label = 'amp'
        verbose_name = 'Subject Requisition'
        verbose_name_plural = 'Subject Laboratory Requisition'
        consent_model = 'amp.screeningconsent'
