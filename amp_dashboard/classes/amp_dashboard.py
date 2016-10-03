
from edc_dashboard.subject import RegisteredSubjectDashboard
from amp.models.subject_visit import SubjectVisit
from amp.models import ScreeningConsent
from amp.models.subject_requisition import SubjectRequisition


class AmpDashboard(RegisteredSubjectDashboard):

    view = 'amp_dashboard'
    dashboard_url_name = 'subject_dashboard_url'
    dashboard_name = 'AMP Dashboard'
    urlpattern_view = 'amp_dashboard.views'
    template_name = 'amp_dashboard.html'
    urlpatterns = [
        RegisteredSubjectDashboard.urlpatterns[0][:-1] +
        '(?P<appointment_code>{appointment_code})/$'] + RegisteredSubjectDashboard.urlpatterns
    urlpattern_options = dict(
        RegisteredSubjectDashboard.urlpattern_options,
        dashboard_model=RegisteredSubjectDashboard.urlpattern_options['dashboard_model'] + '|screeningconsent',
        dashboard_type='subject',
        appointment_code='100|200|400|800|1200|1600|2000|2400|2800|3200|3600|4000|4400|4800|5200|5600|6000|6400|6800|7200|7600|8000|8400|8800|9200', )

    def __init__(self, **kwargs):
        super(AmpDashboard, self).__init__(**kwargs)
        self.subject_dashboard_url = 'subject_dashboard_url'
        self.visit_model = SubjectVisit
        self.dashboard_type_list = ['subject']
        self.membership_form_category = ['screeningconsent', 'enrollment', 'follow_up']
        self.dashboard_models['screening_consent'] = ScreeningConsent
        self.dashboard_models['visit'] = self.visit_model
        self._requisition_model = SubjectRequisition

    def get_context_data(self, **kwargs):
        super(AmpDashboard, self).get_context_data(**kwargs)
        self.context.update(
            home='AMP',
            search_name='amp',
            title='AMP Dashboard',
            subject_dashboard_url=self.subject_dashboard_url,
            screening_consent=self.screening_consent,
            local_results=self.render_labs(),
            enrollment_hiv_status=self.maternal_status_helper.enrollment_hiv_status,
            current_hiv_status=self.maternal_status_helper.hiv_status,
        )
        return self.context

    @property
    def subject_identifier(self):
        pass

    @property
    def screening_consent(self):
        screening_consent = None
        try:
            screening_consent = ScreeningConsent.objects.get(subject_identifier=self.subject_identifier)
        except ScreeningConsent.DoesNotExist:
            try:
                screening_consent = ScreeningConsent.objects.get(pk=self.dashboard_id)
            except ScreeningConsent.DoesNotExist:
                return None
        return screening_consent

    @property
    def latest_visit(self):
        return self.visit_model.objects.filter(
            appointment__registered_subject=self.registered_subject).order_by(
                '-appointment__visit_definition__time_point').first()
