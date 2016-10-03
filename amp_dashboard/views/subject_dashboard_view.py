from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

from edc_base.views import EdcBaseViewMixin
from .appointment_visit_crf_view_mixin import AppointmentSubjectVisitCRFViewMixin
from .locator_results_actions_view_mixin import LocatorResultsActionsViewMixin
from .markey_view_mixin import MarkeyViewMixin


class SubjectDashboardView(
        MarkeyViewMixin,
        AppointmentSubjectVisitCRFViewMixin, LocatorResultsActionsViewMixin, EdcBaseViewMixin, TemplateView):

    template_name = 'amp_dashboard/subject_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            title=settings.PROJECT_TITLE,
            project_name=settings.PROJECT_TITLE,
            site_header=admin.site.site_header,
        )
        return context
