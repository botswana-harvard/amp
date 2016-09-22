from django.db import models
from edc_lab.aliquot.model_mixins import AliquotModelMixin
from edc_lab.aliquot.aliquot import Aliquot
from edc_lab.aliquot.managers import AliquotManager
from amp_lab.models.receive import Receive
from amp_lab.models.aliquot_type import AliquotType
from edc_base.model.models.base_uuid_model import BaseUuidModel


class Aliquot(AliquotModelMixin, Aliquot, BaseUuidModel):

    receive = models.ForeignKey(
        Receive,
        editable=False)

    aliquot_type = models.ForeignKey(
        AliquotType,
        verbose_name="Aliquot Type",
        null=True)

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

    class Meta(AliquotModelMixin.Meta):
        app_label = 'amp_lab'
