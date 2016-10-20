import os
from django.conf import settings
from django.apps import AppConfig

from edc_label.apps import AppConfig as EdcLabelAppConfigParent


class AmpDashboardConfig(AppConfig):
    name = 'amp_dashboard'
    verbose_name = 'amp_dashboard'


class EdcLabelAppConfig(EdcLabelAppConfigParent):
    default_cups_server_ip = '192.168.4.145'
    default_printer_label = 'pharma'
    default_template_folder = os.path.join(settings.STATIC_ROOT, 'templates', 'label_templates')
    extra_templates_folder = os.path.join(settings.STATIC_ROOT, 'templates', 'label_templates')
