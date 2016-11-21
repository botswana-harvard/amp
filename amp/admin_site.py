from django.apps import apps as django_apps
from django.contrib.admin import AdminSite

app_config = django_apps.get_app_config('edc_base')


class AmpAdminSite(AdminSite):
    site_title = app_config.project_name
    site_header = app_config.project_name
    index_title = app_config.project_name
    site_url = '/'
amp_admin = AmpAdminSite(name='amp_admin')


class AmpHistoricalAdminSite(AdminSite):
    site_title = app_config.project_name + ' (Historical)'
    site_header = app_config.project_name + ' (Historical)'
    index_title = app_config.project_name + ' (Historical)'
    site_url = '/'
amp_historical_admin = AmpHistoricalAdminSite(name='amp_historical_admin')
