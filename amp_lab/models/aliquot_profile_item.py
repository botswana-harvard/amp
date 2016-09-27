from django.db import models

from edc_base.model.models import BaseUuidModel
from edc_lab.models import BaseProfileItem

from .aliquot_type import AliquotType
from .aliquot_profile import AliquotProfile


class AliquotProfileItem(BaseProfileItem, BaseUuidModel):

    profile = models.ForeignKey(AliquotProfile)

    aliquot_type = models.ForeignKey(AliquotType)

    def __unicode__(self):
        return str(self.aliquot_type)

    def natural_key(self):
        return self.profile.natural_key() + self.aliquot_type.natural_key()

    class Meta:
        app_label = 'amp_lab'
        unique_together = ('profile', 'aliquot_type')
        db_table = 'amp_lab_profileitem'
