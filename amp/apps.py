import pytz

import os

from datetime import datetime

from django.apps import AppConfig
from django.conf import settings

from edc_appointment.apps import AppConfig as EdcAppointmentAppConfigParent
from edc_base.apps import AppConfig as EdcBaseAppConfigParent
from edc_identifier.apps import AppConfig as EdcIdentifierAppConfigParent
from edc_label.apps import AppConfig as EdcLabelAppConfigParent
from edc_protocol.apps import AppConfig as EdcProtocolAppConfigParent
from edc_registration.apps import AppConfig as EdcRegistrationAppConfigParent
from edc_timepoint.apps import AppConfig as EdcTimepointAppConfig
from edc_timepoint.timepoint import Timepoint
from edc_visit_tracking.apps import AppConfig as EdcVisitTrackingAppConfigParent


class AmpAppConfig(AppConfig):
    name = 'amp'
    protocol_number = 'HVTN 081'
    datafax_site_number = 283
    datafax_site_name = 'Botswana, Gabarone'
    institution = 'Botswana Harvard AIDS Institute Partnership'
    verbose_name = 'AMP Study'
    device_id = 91


class EdcBaseAppConfig(EdcBaseAppConfigParent):
    institution = 'Botswana Harvard AIDS Institute Partnership'
    project_name = 'AMP STUDY'


class EdcIdentifierAppConfig(EdcIdentifierAppConfigParent):
    identifier_prefix = '084'


class EdcTimepointAppConfig(EdcTimepointAppConfig):
    timepoints = [
        Timepoint(
            model='amp.appointment',
            datetime_field='appt_datetime',
            status_field='appt_status',
            closed_status='CLOSED'
        )
    ]


class EdcLabelAppConfig(EdcLabelAppConfigParent):
    default_cups_server_ip = '192.168.4.145'
    default_printer_label = 'amp'
    default_template_folder = os.path.join(settings.BASE_DIR, 'templates', 'static', 'templates', 'label_templates')
    extra_templates_folder = os.path.join(settings.BASE_DIR, 'templates', 'static', 'templates', 'label_templates')


class EdcRegistrationAppConfig(EdcRegistrationAppConfigParent):
    app_label = 'amp'


class EdcProtocolAppConfig(EdcProtocolAppConfigParent):
    name = 'amp'
    protocol = 'AMP'
    protocol_name = 'AMP Study'
    protocol_title = 'AMP Study'
    protocol_number = 'HVTN 081'
    verbose_name = 'AMP Study'
    study_open_datetime = datetime(2016, 7, 20, 0, 0, 0, tzinfo=pytz.timezone('UTC')),
    enrollment_caps = {'amp.enrollment': ('subject', 500)}  # {label_lower: (key, count)}


class EdcAppointmentAppConfig(EdcAppointmentAppConfigParent):
    app_label = 'amp'


class EdcVisitTrackingAppConfig(EdcVisitTrackingAppConfigParent):
    visit_models = {'amp': ('subject_visit', 'amp.subjectvisit')}
