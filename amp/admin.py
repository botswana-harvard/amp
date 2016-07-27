
from django.contrib import admin
from django.core.urlresolvers import reverse
from edc_base.modeladmin.mixins import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin, ModelAdminFormAutoNumberMixin,
    ModelAdminAuditFieldsMixin)

from amp.models import SubjectIdentifier, ScreeningConsent

from .forms import ScreeningConsentForm

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

    fields = ('report_datetime')
    # readonly_fields = ('edd_by_lmp', 'ga_lmp_enrollment_wks', 'enrollment_hiv_status')
    # radio_fields = {'is_diabetic': admin.VERTICAL}
    list_display = ('report_datetime')


#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "registered_subject":
#             if request.GET.get('registered_subject'):
#                 kwargs["queryset"] = RegisteredSubject.objects.filter(
#                     id__exact=request.GET.get('registered_subject', 0))
#             else:
#                 self.readonly_fields = list(self.readonly_fields)
#                 try:
#                     self.readonly_fields.index('registered_subject')
#                 except ValueError:
#                     self.readonly_fields.append('registered_subject')
#         return super(ScreeningConsentAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(ScreeningConsent, ScreeningConsentAdmin)


