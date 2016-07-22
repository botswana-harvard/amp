from django.db import models

from edc_base.model.models import BaseUuidModel
from edc_lab.lab_profile.models import BaseProfile

from .aliquot_type import AliquotType


class AliquotProfile(BaseProfile, BaseUuidModel):

    aliquot_type = models.ForeignKey(
        AliquotType,
        verbose_name='Source aliquot type')

    def natural_key(self):
        return (self.name,)

    class Meta:
        app_label = 'amp_lab'
        db_table = 'amp_lab_profile'
