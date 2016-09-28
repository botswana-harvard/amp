from django.db import models

# from edc_base.audit_trail import AuditTrail
from edc_base.model.models import BaseUuidModel
from edc_constants.constants import NOT_APPLICABLE

from .subject_requisition import SubjectRequisition
from .panel import Panel

from .packing_list import PackingList


class PackingListItem(BasePackingListItem, BaseUuidModel):

    packing_list = models.ForeignKey(PackingList, null=True)

    panel = models.ForeignKey(
        Panel,
        null=True,
        blank=True)

    class Meta:
        app_label = "amp_lab"
        verbose_name = 'Packing List Item'
