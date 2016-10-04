from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

from edc_base.views import EdcBaseViewMixin
from .appointment_visit_crf_view_mixin import AppointmentSubjectVisitCRFViewMixin
from .locator_results_actions_view_mixin import LocatorResultsActionsViewMixin
from .marquee_view_mixin import MarqueeViewMixin
from amp.models.screening_consent import ScreeningConsent
from amp.models.requisition_meta_data import RequisitionMetadata
from datetime import datetime
from amp.models.subject_visit import SubjectVisit
from amp.models.appointment import Appointment


class SubjectDashboardView(
        MarqueeViewMixin,
        AppointmentSubjectVisitCRFViewMixin, LocatorResultsActionsViewMixin, EdcBaseViewMixin, TemplateView):

    context = {}
    template_name = 'amp_dashboard/subject_dashboard.html'

    def get_context_data(self, **kwargs):
        self.context = super().get_context_data(**kwargs)
        self.context.update(
            title=settings.PROJECT_TITLE,
            project_name=settings.PROJECT_TITLE,
            site_header=admin.site.site_header,
        )
        self.context.update({
            'markey_data': self.markey_data,
            'markey_next_row': self.markey_next_row,
            'requisitions': self.requistions,
            'scheduled_forms': self.scheduled_forms
        })
        return self.context

    @property
    def scheduled_forms(self):
        return {}

    @property
    def requistions(self):
        appointment = Appointment.objects.all().order_by('visit_code').first()
        try:
            SubjectVisit.objects.get(appointment__subject_identifier='1001243-1')
        except SubjectVisit.DoesNotExist:
            SubjectVisit.objects.create(
                appointment=appointment,
                report_datetime=datetime.today(),
                reason='scheduled',
            )
        requistions = RequisitionMetadata.objects.filter(subject_identifier='1001243-1')
        return requistions

    @property
    def consent(self):
        try:
            screening_consent = ScreeningConsent.objects.all().first()
        except ScreeningConsent.DoesNotExist:
            screening_consent = None
        return screening_consent

    @property
    def subject_identifier(self):
        subject_identifier = self.context.get('subject_identifier')
        return subject_identifier
