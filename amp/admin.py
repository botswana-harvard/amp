
from django.contrib import admin
from django.core.urlresolvers import reverse
from edc_base.modeladmin.mixins import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin, ModelAdminFormAutoNumberMixin,
    ModelAdminAuditFieldsMixin)

from amp.models import SubjectIdentifier, ScreeningConsent, StudyConsent, SubjectVisit, SubjectOffStudy, SubjectRequisition

from .forms import ScreeningConsentForm, StudyConsentForm, SubjectOffStudyForm, SubjectVisitForm, SubjectRequisitionForm
from .admin_mixin import EdcLabelAdminMixin


admin.register(SubjectIdentifier)


class BaseModelAdmin(ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin, ModelAdminFormAutoNumberMixin,
                     ModelAdminAuditFieldsMixin, admin.ModelAdmin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'

    def redirect_url(self, request, obj, post_url_continue=None):
        url_name = request.GET.get(self.querystring_name)
        section_name = request.GET.get('section_name')
        return reverse(url_name, kwargs={'section_name': section_name})


class MembershipBaseModelAdmin(ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
                               ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin, admin.ModelAdmin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'

    def redirect_url(self, request, obj, post_url_continue=None):
        url_name = request.GET.get(self.querystring_name)
        dashboard_type = request.GET.get('dashboard_type')
        dashboard_model = request.GET.get('dashboard_model')
        dashboard_id = request.GET.get('dashboard_id')
        show = request.GET.get('show')
        return reverse(url_name, kwargs={
            'dashboard_type': dashboard_type,
            'dashboard_model': dashboard_model,
            'dashboard_id': dashboard_id,
            'show': show})


class ScreeningConsentAdmin(MembershipBaseModelAdmin):

    dashboard_type = 'maternal'
    form = ScreeningConsentForm

admin.site.register(ScreeningConsent, ScreeningConsentAdmin)


class StudyConsentAdmin(MembershipBaseModelAdmin):

    dashboard_type = 'maternal'
    form = StudyConsentForm

admin.site.register(StudyConsent, StudyConsentAdmin)


class SubjectOffStudyAdmin(MembershipBaseModelAdmin):

    dashboard_type = 'maternal'
    form = SubjectOffStudyForm

admin.site.register(SubjectOffStudy, SubjectOffStudyAdmin)


class SubjectVisitAdmin(MembershipBaseModelAdmin):

    dashboard_type = 'maternal'
    form = SubjectVisitForm

admin.site.register(SubjectVisit, SubjectVisitAdmin)


class SubjectRequisitionAdmin(EdcLabelAdminMixin, MembershipBaseModelAdmin):

    actions = ['print_requisition_zpl_labels']

    def print_requisition_zpl_labels(self, request, queryset):
        for requisition in queryset:
            self.printer_label('amp_zpl_printer_label', context=requisition.label_context())
    print_requisition_zpl_labels.short_description = "Print requisitions labels"

    dashboard_type = 'maternal'
    form = SubjectRequisitionForm

admin.site.register(SubjectRequisition, SubjectRequisitionAdmin)
