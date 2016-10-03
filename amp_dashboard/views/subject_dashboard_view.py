from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

from edc_base.views import EdcBaseViewMixin
from .appointment_visit_crf_view_mixin import AppointmentSubjectVisitCRFViewMixin
from .locator_results_actions_view_mixin import LocatorResultsActionsViewMixin
from .markey_view_mixin import MarkeyViewMixin
from amp.models.screening_consent import ScreeningConsent


class SubjectDashboardView(
        MarkeyViewMixin,
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
            'markey_next_row': self.markey_next_row
        })
        return self.context

    @property
    def consent(self):
        try:
            screening_consent = ScreeningConsent.objects.get(subject_identifier=self.subject_identifier)
        except ScreeningConsent.DoesNotExist:
            screening_consent = None
        return screening_consent

    @property
    def subject_identifier(self):
        subject_identifier = self.context.get('subject_identifier')
        return subject_identifier
