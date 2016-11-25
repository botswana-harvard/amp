from django.contrib import admin
from django.core.urlresolvers import reverse

from edc_base.modeladmin_mixins import (ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
                                        ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin)
from edc_visit_tracking.modeladmin_mixins import VisitModelAdminMixin

from .admin_site import amp_admin
from .forms import ScreeningConsentForm, SubjectOffStudyForm, SubjectVisitForm, AppointmentForm
from .models import SubjectIdentifier, ScreeningConsent, SubjectVisit, SubjectOffstudy, Appointment


class BaseModelAdmin(ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin, ModelAdminFormAutoNumberMixin,
                     ModelAdminAuditFieldsMixin, admin.ModelAdmin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'

    def redirect_url(self, request, obj, post_url_continue=None):
        url_name = request.GET.get(self.querystring_name)
        section_name = request.GET.get('section_name')
        return reverse(url_name, kwargs={'section_name': section_name})


class AmpBaseModelAdmin(ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
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
class AppointmentAdmin(AmpBaseModelAdmin):

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

    def save_model(self, request, obj, form, change):
        subject_identifier = request.GET.get('subject_identifier')
        visit_code = request.GET.get('visit_code')
        visit_schedule_name = request.GET.get('visit_schedule_name')
        schedule_name = request.GET.get('schedule_name')
        obj.subject_identifier = subject_identifier
        obj.visit_code_sequence = self.new_visit_code_sequence(visit_code, subject_identifier)
        obj.visit_code = self.new_visit_code(visit_code, subject_identifier)
        obj.visit_schedule_name = visit_schedule_name
        obj.schedule_name = schedule_name
        super(AppointmentAdmin, self).save_model(request, obj, form, change)

    def new_visit_code(self, visit_code, subject_identifier):
        return round(float(self.previous_appt(visit_code, subject_identifier).visit_code) + 0.1, 1)

    def new_visit_code_sequence(self, visit_code, subject_identifier):
        return str(int(self.previous_appt(visit_code, subject_identifier).visit_code_sequence) + 1)

    def previous_appt(self, visit_code, subject_identifier):
        appts = []
        for ap in Appointment.objects.filter(subject_identifier=subject_identifier):
            parent_appt_visit_code = int(float(visit_code))
            appt_visit_code = int(float(ap.visit_code))
            if appt_visit_code < (parent_appt_visit_code + 1) and appt_visit_code >= parent_appt_visit_code:
                appts.append(ap.pk)
        appontment = Appointment.objects.filter(pk__in=appts).latest('created')
        return appontment


@admin.register(ScreeningConsent, site=amp_admin)
class ScreeningConsentAdmin(AmpBaseModelAdmin):
    fields = (
        'subject_identifier',
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


@admin.register(SubjectOffstudy, site=amp_admin)
class SubjectOffStudyAdmin(AmpBaseModelAdmin):

    dashboard_type = 'maternal'
    form = SubjectOffStudyForm


@admin.register(SubjectVisit, site=amp_admin)
class SubjectVisitAdmin(VisitModelAdminMixin, AmpBaseModelAdmin):
    form = SubjectVisitForm
