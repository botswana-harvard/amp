
from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import AdminRadioSelect, AdminRadioFieldRenderer

from django.core.urlresolvers import reverse
from edc_base.modeladmin.mixins import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin, ModelAdminFormAutoNumberMixin,
    ModelAdminAuditFieldsMixin)

from amp.models import SubjectIdentifier, ScreeningConsent, StudyConsent, SubjectVisit, SubjectOffStudy, SubjectRequisition

from edc_visit_tracking.admin import VisitAdminMixin

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
        url_name = 'subject_dashboard_url'
        print(request.GET)
        subject_identifier = request.GET.get('subject_identifier')
        return reverse(url_name, kwargs={
            'subject_identifier': subject_identifier})


class ScreeningConsentAdmin(MembershipBaseModelAdmin):
    fields = (
        'first_name',
        'last_name',
        'initials',
        'language',
        'study_site',
        'is_literate',
        'witness_name',
        'consent_datetime',
        'dob',
        'is_dob_estimated',
        'citizen',
        'identity',
        'identity_type',
        'confirm_identity',
        'comment',
        'consent_reviewed',
        'study_questions',
        'assessment_score',
        'consent_signature',
        'consent_copy'
    )

    search_fields = ('subject_identifier', 'id', 'identity', 'first_name', 'last_name')

    radio_fields = {
        'assessment_score': admin.VERTICAL,
        'citizen': admin.VERTICAL,
        'consent_copy': admin.VERTICAL,
        'consent_reviewed': admin.VERTICAL,
        'consent_signature': admin.VERTICAL,
        'identity_type': admin.VERTICAL,
        'is_dob_estimated': admin.VERTICAL,
        'is_literate': admin.VERTICAL,
        'language': admin.VERTICAL,
        'study_questions': admin.VERTICAL}

    list_display = ('dashboard',
                    'subject_identifier',
                    'is_verified',
                    'is_verified_datetime',
                    'first_name',
                    'initials',
                    'gender',
                    'dob',
                    'consent_datetime',
                    'created',
                    'modified',
                    'user_created',
                    'user_modified')
    list_filter = ('language',
                   'is_verified',
                   'is_literate',
                   'identity_type')

    dashboard_type = 'subject'
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


class SubjectVisitAdmin(VisitAdminMixin, MembershipBaseModelAdmin):
    form = SubjectVisitForm

admin.site.register(SubjectVisit, SubjectVisitAdmin)


class SubjectRequisitionAdmin(EdcLabelAdminMixin, MembershipBaseModelAdmin):
    panel_model = None
    date_hierarchy = 'requisition_datetime'

    fields = [
        'subject_visit',
        'report_datetime',
        "requisition_datetime",
        "is_drawn",
        "reason_not_drawn",
        "drawn_datetime",
        "panel_name",
        "item_type",
        "estimated_volume",
        "comments",
    ]

    radio_fields = {
        "is_drawn": admin.VERTICAL,
        "reason_not_drawn": admin.VERTICAL,
        "item_type": admin.VERTICAL,
    }

    list_display = [
        'dashboard',
        'requisition_identifier',
        'specimen_identifier',
        'subject',
        "requisition_datetime",
        "panel_name",
        'hostname_created',
    ]

    list_filter = [
        'panel_name',
        "requisition_datetime",
        'study_site',
        'user_created',
        'hostname_created',
        'user_modified',
    ]
    search_fields = [
        'specimen_identifier',
        'requisition_identifier',
        'panel_name'
    ]

    actions = ['print_requisition_zpl_labels']

    def print_requisition_zpl_labels(self, request, queryset):
        for requisition in queryset:
            self.printer_label('amp_zpl_printer_label', context=requisition.label_context())
    print_requisition_zpl_labels.short_description = "Print requisitions labels"

    form = SubjectRequisitionForm
    label_template_name = 'requisition_label'
    visit_attr = 'subject_visit'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "subject_visit":
            kwargs["queryset"] = SubjectVisit.objects.filter(
                subject_identifier=request.GET.get('subject_identifier', ''))
        return super(SubjectRequisitionAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(SubjectRequisition, SubjectRequisitionAdmin)
