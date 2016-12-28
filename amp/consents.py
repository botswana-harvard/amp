import arrow

from dateutil.tz.tz import gettz
from datetime import datetime

from django.apps import apps as django_apps

from edc_consent.consent import Consent
from edc_consent.site_consents import site_consents
from edc_constants.constants import MALE, FEMALE

app_config = django_apps.get_app_config('edc_protocol')

subjectconsent_v1 = Consent(
    'amp.screeningconsent',
    version='1',
    start=arrow.get(datetime(2016, 5, 1, 0, 0, 0), tzinfo=gettz('Africa/Gaborone')).to('UTC').datetime,
    end=arrow.get(datetime(2020, 10, 30, 0, 0, 0), tzinfo=gettz('Africa/Gaborone')).to('UTC').datetime,
    age_min=16,
    age_is_adult=18,
    age_max=64,
    gender=[MALE, FEMALE])

site_consents.register(subjectconsent_v1)
