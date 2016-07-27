from collections import OrderedDict

from edc_visit_schedule.classes import (
    VisitScheduleConfiguration, site_visit_schedules, MembershipFormTuple, ScheduleTuple)

from ..models import StudyConsent

from .entries import *
from amp.models.subject_visit import SubjectVisit
from amp.visit_schedule.requistions_entries import (
    visit_2000_requisition, visit_400_requisition, visit_200_requisition, visit_9200_requisition,
    visit_800_requisition, visit_1200_requisition, visit_1600_requisition, visit_2400_requisition,
    visit_2800_requisition, visit_3200_requisition, visit_3600_requisition, visit_4000_requisition,
    visit_4400_requisition, visit_4800_requisition, visit_5600_requisition, visit_5200_requisition,
    visit_6000_requisition, visit_6400_requisition, visit_6800_requisition, visit_7200_requisition,
    visit_7600_requisition, visit_8000_requisition, visit_8400_requisition, visit_8800_requisition,
)


class StudyConsentSchedule(VisitScheduleConfiguration):

    name = 'Study Consent Visit Schedule'
    app_label = 'amp'

    membership_forms = OrderedDict({'studyconsent': MembershipFormTuple(
        'studyconsent', StudyConsent, True), })

    schedules = OrderedDict({
        'Study Consent': ScheduleTuple('Follow Up Visit', 'studyconsent', None, None), })

    visit_definitions = OrderedDict()

    visit_definitions['200'] = {
        'title': '1 Weeks Visit',
        'time_point': 50,
        'base_interval': 1,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_200_requisition,
        'entries': None}

    visit_definitions['400'] = {
        'title': '4 Weeks',
        'time_point': 110,
        'base_interval': 2,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_400_requisition,
        'entries': (), }

    visit_definitions['800'] = {
        'title': '8 Weeks Visit',
        'time_point': 170,
        'base_interval': 6,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_800_requisition,
        'entries': ()}

    visit_definitions['1200'] = {
        'title': '12 Weeks Visit',
        'time_point': 230,
        'base_interval': 12,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_1200_requisition,
        'entries': ()}

    visit_definitions['1600'] = {
        'title': '16 Weeks Visit',
        'time_point': 290,
        'base_interval': 18,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_1600_requisition,
        'entries': (), }

    visit_definitions['2000'] = {
        'title': '20 Weeks Visit',
        'time_point': 350,
        'base_interval': 24,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_2000_requisition,
        'entries': ()}

    visit_definitions['2400'] = {
        'title': '24 Weeks Visit',
        'time_point': 410,
        'base_interval': 30,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_2400_requisition,
        'entries': (), }

    visit_definitions['2800'] = {
        'title': '28 Weeks Visit',
        'time_point': 410,
        'base_interval': 36,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_2800_requisition,
        'entries': (), }

    visit_definitions['3200'] = {
        'title': '32 Weeks Visit',
        'time_point': 420,
        'base_interval': 42,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_3200_requisition,
        'entries': (), }

    visit_definitions['3600'] = {
        'title': '36 Weeks Visit',
        'time_point': 430,
        'base_interval': 43,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_3600_requisition,
        'entries': (), }

    visit_definitions['4000'] = {
        'title': '40 Weeks Visit',
        'time_point': 440,
        'base_interval': 44,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_4000_requisition,
        'entries': (), }

    visit_definitions['4400'] = {
        'title': '44 Weeks Visit',
        'time_point': 450,
        'base_interval': 45,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_4400_requisition,
        'entries': (), }

    visit_definitions['4800'] = {
        'title': '48 Weeks Visit',
        'time_point': 460,
        'base_interval': 46,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_4800_requisition,
        'entries': (), }

    visit_definitions['5200'] = {
        'title': '52 Weeks Visit',
        'time_point': 470,
        'base_interval': 47,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_5200_requisition,
        'entries': (), }

    visit_definitions['5600'] = {
        'title': '56 Weeks Visit',
        'time_point': 480,
        'base_interval': 48,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_5600_requisition,
        'entries': (), }

    visit_definitions['6000'] = {
        'title': '60 Weeks Visit',
        'time_point': 490,
        'base_interval': 49,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_6000_requisition,
        'entries': (), }

    visit_definitions['6400'] = {
        'title': '64 Weeks Visit',
        'time_point': 500,
        'base_interval': 50,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_6400_requisition,
        'entries': (), }

    visit_definitions['6800'] = {
        'title': '68 Weeks Visit',
        'time_point': 510,
        'base_interval': 51,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_6800_requisition,
        'entries': (), }

    visit_definitions['7200'] = {
        'title': '72 Weeks Visit',
        'time_point': 520,
        'base_interval': 52,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_7200_requisition,
        'entries': (), }

    visit_definitions['7600'] = {
        'title': '76 Weeks Visit',
        'time_point': 530,
        'base_interval': 53,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_7600_requisition,
        'entries': (), }

    visit_definitions['8000'] = {
        'title': '80 Weeks Visit',
        'time_point': 540,
        'base_interval': 54,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_8000_requisition,
        'entries': (), }

    visit_definitions['8400'] = {
        'title': '84 Weeks Visit',
        'time_point': 550,
        'base_interval': 55,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_8400_requisition,
        'entries': (), }

    visit_definitions['8800'] = {
        'title': '88 Weeks Visit',
        'time_point': 560,
        'base_interval': 56,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_8800_requisition,
        'entries': (), }

    visit_definitions['9200'] = {
        'title': '92 Weeks Visit',
        'time_point': 560,
        'base_interval': 56,
        'base_interval_unit': 'M',
        'window_lower_bound': 0,
        'window_lower_bound_unit': 'D',
        'window_upper_bound': 0,
        'window_upper_bound_unit': 'D',
        'grouping': 'maternal',
        'visit_tracking_model': SubjectVisit,
        'schedule': 'Follow Up Visit',
        'instructions': '',
        'requisitions': visit_9200_requisition,
        'entries': (), }

site_visit_schedules.register(StudyConsentSchedule)
