from edc_lab.aliquot.aliquot_type import AliquotType


class AliquotType(AliquotType):

    class Meta:
        app_label = 'amp_lab'
        ordering = ["name"]
