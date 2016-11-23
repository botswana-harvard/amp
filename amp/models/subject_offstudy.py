from django.db import models

from edc_base.model.models import BaseUuidModel, HistoricalRecords
from edc_offstudy.model_mixins import OffstudyModelMixin


class SubjectOffstudy(OffstudyModelMixin, BaseUuidModel):

    objects = models.Manager()

    history = HistoricalRecords()

    class Meta:
        app_label = 'amp'
        visit_schedule_name = 'subject_visit_schedule'
        consent_model = 'amp.screeningconsent'
