from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

from edc_base.views import EdcBaseViewMixin
from .appointment_visit_crf_view_mixin import AppointmentSubjectVisitCRFViewMixin
from .locator_results_actions_view_mixin import LocatorResultsActionsViewMixin
from .marquee_view_mixin import MarqueeViewMixin
from amp.models.screening_consent import ScreeningConsent
from amp.models.requisition_meta_data import RequisitionMetadata
from edc_label.view_mixins import EdcLabelViewMixin
from amp.constants import SUBJECT
from amp.apps import AmpAppConfig
from amp.models.appointment import Appointment


class SubjectDashboardView(
        MarqueeViewMixin,
        AppointmentSubjectVisitCRFViewMixin, LocatorResultsActionsViewMixin, EdcBaseViewMixin, EdcLabelViewMixin, TemplateView):

    def __init__(self, **kwargs):
        super(SubjectDashboardView, self).__init__(**kwargs)
        self.request = None
        self.screening_consent = None
        self.context = {}
        self.show = None
        self.template_name = 'amp_dashboard/subject_dashboard.html'
        super(EdcLabelViewMixin, self).__init__()

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
            'requisitions_meta_data': {},   # self.requisitions_meta_data
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
        self.print_barcode_label(request)
        return self.render_to_response(context)

    def label_context(self, visit_code, extra_context=None):
        context = {}
        context.update({
            'dob': self.screening_consent.dob,
            'gender': self.screening_consent.gender,
            'initials': self.screening_consent.initials,
            'protocol': AmpAppConfig.protocol_number,
            'site': '12701',
            'subject_identifier': self.screening_consent.subject_identifier,
            'visit_code': visit_code,
        })
        return context

    def print_barcode_label(self, request, copies=1, context=None):
        if request:
            subject_identifier = request.GET.get('subject_identifier')
            appointment_pk = request.GET.get('appointment_pk')
            try:
                appointment = Appointment.objects.get(pk=appointment_pk)
            except Appointment.DoesNotExist:
                pass
        if subject_identifier and appointment_pk:
            self.screening_consent = ScreeningConsent.objects.get(subject_identifier=subject_identifier)
            print_value = request.GET.get('print', None)
            if print_value:
                copies = 1 if copies is None else copies
                label_template = 'amp_requisition_label_template'
                context = self.label_context(appointment.visit_code)
                super(SubjectDashboardView, self).print_label(
                    label_template, copies=copies, context=context)

    @property
    def scheduled_forms(self):
        return {}

    @property
    def requisitions_meta_data(self):
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
