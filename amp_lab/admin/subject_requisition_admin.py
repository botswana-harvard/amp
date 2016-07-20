from copy import copy

from django.contrib import admin

from lab_requisition.admin import RequisitionAdminMixin

from amp.base_model_admin import BaseModelAdmin
from ..forms import SubjectRequisitionForm
from ..models import SubjectRequisition, Panel


class SubjectRequisitionAdmin(RequisitionAdminMixin, BaseModelAdmin):

    form = SubjectRequisitionForm
    label_template_name = 'requisition_label'
    visit_attr = 'subject_visit'
    #visit_model = SubjectVisit
    panel_model = Panel

    def get_fieldsets(self, request, obj=None):
        fields = copy(self.fields)
        try:
            panel = Panel.objects.get(id=request.GET.get('panel'))
            if panel.name in ['Rectal swab (Storage)']:
                try:
                    fields.remove(fields.index('estimated_volume'))
                except ValueError:
                    pass
        except self.panel_model.DoesNotExist:
            pass
        try:
            fields.remove(fields.index('test_code'))
        except ValueError:
            pass
        return [(None, {'fields': fields})]

admin.site.register(SubjectRequisition, SubjectRequisitionAdmin)
