from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

from edc_base.views import EdcBaseViewMixin
from .appointment_visit_crf_view_mixin import AppointmentSubjectVisitCRFViewMixin
from .locator_results_actions_view_mixin import LocatorResultsActionsViewMixin
from .marquee_view_mixin import MarqueeViewMixin
from amp.models.screening_consent import ScreeningConsent
from amp.models.requisition_meta_data import RequisitionMetadata
from amp.models.subject_requisition import SubjectRequisition
from django.http.response import HttpResponse
from edc_label.view_mixins import EdcLabelViewMixin
import json
from amp.constants import SUBJECT


class SubjectDashboardView(
        MarqueeViewMixin,
        AppointmentSubjectVisitCRFViewMixin, LocatorResultsActionsViewMixin, EdcBaseViewMixin, EdcLabelViewMixin, TemplateView):

    def __init__(self, **kwargs):
        super(SubjectDashboardView, self).__init__(**kwargs)
        self.request = None
        self.context = {}
        self.show = None
        self.template_name = 'amp_dashboard/subject_dashboard.html'

    def get_context_data(self, **kwargs):
        self.context = super().get_context_data(**kwargs)
        self.context.update(
            title=settings.PROJECT_TITLE,
            project_name=settings.PROJECT_TITLE,
            site_header=admin.site.site_header,
        )
        self.context.update({
            'markey_data': self.markey_data.items(),
            'markey_next_row': self.markey_next_row,
            'requisitions': self.requistions,
            'scheduled_forms': self.scheduled_forms,
            'appointments': self.appointments,
            'subject_identifier': self.subject_identifier,
            'consents': [("Screening Consent(complete)", self.consent)],
            'dashboard_type': SUBJECT
        })
        return self.context

    def get(self, request, *args, **kwargs):
        self.request = request
        context = self.get_context_data(**kwargs)
        self.show = request.GET.get('show', None)
        context.update({'show': self.show})
        self.print_barcode_labels(request)
        return self.render_to_response(context)

    def print_barcode_labels(self, request):
        print_status = False
        result = {}
        if request.is_ajax():
            requisitionsIds = request.GET.get('requisitionids')
            for requisition_id in requisitionsIds:
                try:
                    subject_requistion = SubjectRequisition.objects.get(pk=requisition_id)
                    super(SubjectDashboardView, self).print_label(
                        'amp_requisition_label_template', context=subject_requistion.label_context())
                    print_status = True
                except SubjectRequisition.DoesNotExist:
                    pass
            result = {'labels_printed': len(requisitionsIds)}
        if print_status:
            return HttpResponse(json.dumps(result), content_type='application/json')

    @property
    def scheduled_forms(self):
        return {}

    @property
    def requistions(self):
        requistions = RequisitionMetadata.objects.filter(
            subject_identifier=self.subject_identifier, appointment=self.appointment)
        return requistions

    @property
    def consent(self):
        try:
            screening_consent = ScreeningConsent.objects.get(subject_identifier=self.subject_identifier)
        except ScreeningConsent.DoesNotExist:
            screening_consent = None
        return screening_consent

    @property
    def show_forms(self):
        show = self.request.GET.get('show', None)
        return True if show == 'forms' else False

    @property
    def subject_identifier(self):
        return self.context.get('subject_identifier')
