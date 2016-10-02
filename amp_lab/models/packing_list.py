from edc_base.model.models import BaseUuidModel
from edc_lab.packing.model_mixins import PackingListModelMixin


class PackingList(PackingListModelMixin, BaseUuidModel):


#     @property
#     def item_models(self):
#         item_m = []
#         item_m.append(models.get_model('mb_lab', 'InfantRequisition'))
#         item_m.append(models.get_model('mb_lab', 'MaternalRequisition'))
#         item_m.append(models.get_model('mb_lab', 'Aliquot'))
#         return item_m

#     @property
#     def packing_list_item_model(self):
#         return models.get_model('mb_lab', 'PackingListItem')

    class Meta:
        app_label = 'amp_lab'
        verbose_name = 'Packing List'
