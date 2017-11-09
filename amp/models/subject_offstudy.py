from django.db import models

from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_offstudy.model_mixins import OffstudyModelMixin


class SubjectOffstudy(OffstudyModelMixin, BaseUuidModel):

    objects = models.Manager()

#     history = HistoricalRecords()

    class Meta:
        app_label = 'amp'
        visit_schedule_name = 'visit_schedule1.schedule1'
        consent_model = 'amp.screeningconsent'
