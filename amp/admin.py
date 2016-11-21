from django.contrib import admin
from django.core.urlresolvers import reverse


from edc_base.modeladmin.mixins import (ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
                                        ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin)
from edc_visit_tracking.admin import VisitAdminMixin

from .admin_mixin import EdcLabelAdminMixin
from .admin_site import amp_admin
from .forms import ScreeningConsentForm, SubjectOffStudyForm, SubjectVisitForm, SubjectRequisitionForm, AppointmentForm
from .models import SubjectIdentifier, ScreeningConsent, SubjectVisit, SubjectOffStudy, SubjectRequisition, Appointment


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
        return request.GET.get('next')


@admin.register(SubjectIdentifier, site=amp_admin)
class SubjectIdentifierAdmin(admin.ModelAdmin):
    pass


@admin.register(Appointment, site=amp_admin)
class AppointmentAdmin(MembershipBaseModelAdmin):

    fields = (
        'appt_datetime',
        'appt_type',
        'appt_status',
        'appt_reason',
        'comment',
    )

    radio_fields = {
        'appt_type': admin.VERTICAL,
        'appt_status': admin.VERTICAL}

    form = AppointmentForm


@admin.register(ScreeningConsent, site=amp_admin)
class ScreeningConsentAdmin(MembershipBaseModelAdmin):
    fields = (
        'first_name',
        'last_name',
        'initials',
        'gender',
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
        'gender': admin.VERTICAL,
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


@admin.register(SubjectOffStudy, site=amp_admin)
class SubjectOffStudyAdmin(MembershipBaseModelAdmin):

    dashboard_type = 'maternal'
    form = SubjectOffStudyForm


@admin.register(SubjectVisit, site=amp_admin)
class SubjectVisitAdmin(VisitAdminMixin, MembershipBaseModelAdmin):
    form = SubjectVisitForm


@admin.register(SubjectRequisition, site=amp_admin)
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

    actions = ['print_requisition_barcode_labels']

    def print_requisition_barcode_labels(self, request, queryset):
        for requisition in queryset:
            self.print_barcode_label('amp_requisition_label_template', context=requisition.label_context())
    print_requisition_barcode_labels.short_description = "Print requisitions labels"

    form = SubjectRequisitionForm
    label_template_name = 'requisition_label'
    visit_attr = 'subject_visit'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "subject_visit":
            kwargs["queryset"] = SubjectVisit.objects.filter(
                subject_identifier=request.GET.get('subject_identifier', 0))
        return super(SubjectRequisitionAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
