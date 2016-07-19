from edc_base.model.models import BaseUuidModel
from edc_identifier.models import BaseIdentifierModel


class OrderIdentifierHistory(BaseIdentifierModel, BaseUuidModel):

    class Meta:
        app_label = 'amp_lab'
