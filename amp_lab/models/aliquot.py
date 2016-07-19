from django.db import models

# from edc_base.audit_trail import AuditTrail
from edc_base.model.models import BaseUuidModel
from lis.specimen.lab_aliquot.managers import AliquotManager
from lis.specimen.lab_aliquot.models import BaseAliquot

from .aliquot_condition import AliquotCondition
from .aliquot_type import AliquotType
from .receive import Receive


class Aliquot(BaseAliquot, BaseUuidModel):

    receive = models.ForeignKey(
        Receive,
        editable=False)

    aliquot_type = models.ForeignKey(
        AliquotType,
        verbose_name="Aliquot Type",
        null=True)

    aliquot_condition = models.ForeignKey(
        AliquotCondition,
        verbose_name="Aliquot Condition",
        null=True,
        blank=True)

    is_rejected = models.BooleanField(
        verbose_name='rejected',
        default=False)

    objects = AliquotManager()

    def save(self, *args, **kwargs):
        self.subject_identifier = self.receive.registered_subject.subject_identifier
        super(Aliquot, self).save(*args, **kwargs)

    @property
    def specimen_identifier(self):
        return self.aliquot_identifier[:-4]

    @property
    def registered_subject(self):
        return self.receive.registered_subject

    @property
    def visit_code(self):
        return self.receive.visit

    class Meta:
        app_label = 'amp_lab'
        unique_together = (('receive', 'count'), )
