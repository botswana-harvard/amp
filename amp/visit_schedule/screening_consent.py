from collections import OrderedDict

from edc_visit_schedule.classes import (
    VisitScheduleConfiguration, site_visit_schedules, MembershipFormTuple, ScheduleTuple)

from ..models import ScreeningConsent, SubjectVisit

from .requistions_entries import visit_100_requisition


class ScreeningConsentVisitSchedule(VisitScheduleConfiguration):

    name = 'screening consent visit schedule'
    app_label = 'amp'

    membership_forms = OrderedDict({'screeningconsent': MembershipFormTuple(
        'screeningconsent', ScreeningConsent, True), })

    schedules = OrderedDict({
        'Subject Consent': ScheduleTuple('Screening Consent', 'screeningconsent', None, None), })

    visit_definitions = OrderedDict()

    visit_definitions['100'] = {
        'title': 'Maternal Enrollment Visit',
        'time_point': 0,
        'base_interval': 0,
        'base_interval_unit': 'D',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Screening Consent',
        'instructions': '',
        'requisitions': visit_100_requisition,
        'entries': (), }

site_visit_schedules.register(ScreeningConsentVisitSchedule)
