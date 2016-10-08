from edc_base.model.models import BaseUuidModel
from edc_lab.packing.model_mixins import PackingListModelMixin


class PackingList(PackingListModelMixin, BaseUuidModel):

    class Meta:
        app_label = 'amp'
        verbose_name = 'Packing List'
