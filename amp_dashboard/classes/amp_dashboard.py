# from collections import OrderedDict
# from django.utils import timezone

# from edc_registration.models import RegisteredSubject
# from edc_base.utils import convert_from_camel
# from edc_constants.constants import YES, POS, NEG, IND, NEVER, UNKNOWN, DWTA, OTHER
# from edc_dashboard.subject import RegisteredSubjectDashboard
from amp.models.subject_visit import SubjectVisit
from amp.models import SubjectRequisition
from amp.models import ScreeningConsent


class AmpDashboard():

    view = 'amp_dashboard'
    dashboard_url_name = 'subject_dashboard_url'
    dashboard_name = 'AMP Dashboard'
    urlpattern_view = 'mp_dashboard.views'
    template_name = 'amp_dashboard.html'
#     urlpatterns = [
#         RegisteredSubjectDashboard.urlpatterns[0][:-1] +
#         '(?P<appointment_code>{appointment_code})/$'] + RegisteredSubjectDashboard.urlpatterns
#     urlpattern_options = dict(
#         RegisteredSubjectDashboard.urlpattern_options,
#         dashboard_model=RegisteredSubjectDashboard.urlpattern_options['dashboard_model'] + '|screeningconsent',
#         dashboard_type='subject',
#         appointment_code='100|200|400|800|1200|1600|2000|2400|2800|3200|3600|4000|4400|4800|5200|5600|6000|6400|6800|7200|7600|8000|8400|8800|9200', )

    def __init__(self, **kwargs):
        super(AmpDashboard, self).__init__(**kwargs)
        self.subject_dashboard_url = 'subject_dashboard_url'
        self.visit_model = SubjectVisit
        self.dashboard_type_list = ['subject']
        self.membership_form_category = ['screeningconsent', 'follow_up']
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
            local_results=self.render_labs(),
            enrollment_hiv_status=self.maternal_status_helper.enrollment_hiv_status,
            current_hiv_status=self.maternal_status_helper.hiv_status,
        )
        return self.context

#     @property
#     def latest_visit(self):
#         return self.visit_model.objects.filter(
#             appointment__registered_subject=self.registered_subject).order_by(
#                 '-appointment__visit_definition__time_point').first()

#     def get_locator_scheduled_visit_code(self):
#         """ Returns visit where the locator is scheduled, TODO: maybe search visit definition for this?."""
#         return '1000M'

#     @property
#     def maternal_locator(self):
#         return self.locator_model.objects.get(
#             maternal_visit__appointment__registered_subject__subject_identifier=self.subject_identifier)
#
#     @property
#     def subject_identifier(self):
#         return self.registered_subject.subject_identifier




