from edc_lab.packing.forms_mixins import PackingListFormMixin, PackingListItemFormMixin

from ..models import SubjectRequisition
from amp_lab.models.packing_list import PackingList
from edc_lab.models import PackingListItem


class PackingListForm (PackingListFormMixin):

    def clean(self):
        self.requisition = [SubjectRequisition]
        return super(PackingListForm, self).clean()

    class Meta:
        model = PackingList
        fields = '__all__'


class PackingListItemForm (PackingListItemFormMixin):

    def clean(self):
        self.requisition = [SubjectRequisition]
        return super(PackingListItemFormMixin, self).clean()

    class Meta:
        model = PackingListItem
        fields = '__all__'
