from django.db import models

from edc_base.model.models.base_uuid_model import BaseUuidModel

from edc_visit_tracking.model_mixins import CrfModelMixin
from edc_visit_tracking.managers import CrfModelManager
from edc_consent.model_mixins import RequiresConsentMixin

from edc_metadata.model_mixins import UpdatesRequisitionMetadataModelMixin


from edc_lab.requisition.model_mixins import RequisitionModelMixin
from edc_lab.requisition.managers import RequisitionManager
from amp.models.subject_visit import SubjectVisit
from amp_lab.models.packing_list import PackingList
from django.core.urlresolvers import reverse


class SubjectRequisitionManager(CrfModelManager):

    def get_by_natural_key(self, requisition_identifier):
        return self.get(requisition_identifier=requisition_identifier)


class SubjectRequisition(CrfModelMixin, RequisitionModelMixin, RequiresConsentMixin,
                         UpdatesRequisitionMetadataModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    packing_list = models.ForeignKey(PackingList, null=True, blank=True)

    objects = RequisitionManager()

    def dashboard(self):
        """Returns a hyperink for the Admin page."""
        url = reverse(
            'subject_dashboard_url',
            kwargs={
                'dashboard_type': self.registered_subject.subject_type.lower(),
                'dashboard_model': 'appointment',
                'dashboard_id': self.pk,
                'show': 'appointments'
            })
        ret = """<a href="{url}" />dashboard</a>""".format(url=url)
        return ret
    dashboard.allow_tags = True

    def label_context(self, extra_context=None):
        context = {}
        may_store_samples = None
        context.update({
            'barcode_value': self.barcode_value(),
            'clinician_initials': self.user_created[0:2].upper(),
            'dob': self.registered_subject.dob,
            'drawn_datetime': self.drawn_datetime,
            'gender': self.registered_subject.gender,
            'initials': self.registered_subject.initials,
            'item_count': self.item_count,
            'may_store_samples': may_store_samples,
            'panel': self.panel.name[0:21],
            'protocol': '',  # edc_base_app_config.protocol_number
            'requisition_identifier': self.requisition_identifier,
            'site': self.study_site,
            'specimen_identifier': self.specimen_identifier,
            'subject_identifier': self.subject_identifier,
            'visit': self.subject_visit.appointment.visit_code,
        })
        return context

    def get_visit(self):
        return self.subject_visit

    class Meta:
        app_label = 'amp'
        verbose_name = 'Subject Requisition'
        verbose_name_plural = 'Subject Laboratory Requisition'
        consent_model = 'amp.screeningconsent'
