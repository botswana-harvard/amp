from lis.specimen.lab_aliquot_list.models import BaseAliquotType


class AliquotType(BaseAliquotType):

    class Meta:
        app_label = 'amp_lab'
        ordering = ["name"]
