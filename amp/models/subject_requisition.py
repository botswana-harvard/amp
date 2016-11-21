from django.core.urlresolvers import reverse
from django.db import models


from edc_base.model.models.base_uuid_model import BaseUuidModel
from edc_consent.model_mixins import RequiresConsentMixin
from edc_lab.requisition.managers import RequisitionManager
from edc_lab.requisition.model_mixins import RequisitionModelMixin
from edc_metadata.model_mixins import UpdatesRequisitionMetadataModelMixin
from edc_visit_tracking.managers import CrfModelManager
from edc_visit_tracking.model_mixins import CrfModelMixin

from ..apps import AmpAppConfig
from .packing_list import PackingList
from .subject_visit import SubjectVisit
from .screening_consent import ScreeningConsent


class SubjectRequisitionManager(CrfModelManager):

    def get_by_natural_key(self, requisition_identifier):
        return self.get(requisition_identifier=requisition_identifier)


class SubjectRequisition(CrfModelMixin, RequisitionModelMixin, RequiresConsentMixin,
                         UpdatesRequisitionMetadataModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    packing_list = models.ForeignKey(PackingList, null=True, blank=True)

    objects = RequisitionManager()

    def subject(self):
        return None

    def dashboard(self):
        """Returns a hyperink for the Admin page."""
        url = reverse(
            'subject_dashboard_url',
            kwargs={
                'subject_identifier': self.subject_visit.appointment.subject_identifier
            })
        ret = """<a href="{url}" >dashboard</a>""".format(url=url)
        return ret
    dashboard.allow_tags = True

    def label_context(self, extra_context=None):
        context = {}
        may_store_samples = None
        context.update({
#             'barcode_value': self.barcode_value(),
            'clinician_initials': self.user_created[0:2].upper(),
            'dob': self.screening_consent.dob,
            'drawn_datetime': self.drawn_datetime.date(),
            'gender': self.screening_consent.gender,
            'initials': self.screening_consent.initials,
            'item_count': self.item_count,
            'may_store_samples': may_store_samples,
            'protocol': AmpAppConfig.protocol_number,
            'site': self.study_site or '12701',
            'specimen_identifier': self.specimen_identifier,
            'subject_identifier': self.screening_consent.subject_identifier,
            'visit': self.subject_visit.appointment.visit_code,
        })
        return context

    @property
    def screening_consent(self):
        try:
            screening_consent = ScreeningConsent.objects.get(subject_identifier=self.subject_visit.subject_identifier)
        except ScreeningConsent.DoesNotExist:
            screening_consent = None
        return screening_consent

    def get_visit(self):
        return self.subject_visit

    class Meta:
        app_label = 'amp'
        verbose_name = 'Subject Requisition'
        verbose_name_plural = 'Subject Laboratory Requisition'
        consent_model = 'amp.screeningconsent'
