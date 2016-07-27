from django.core.exceptions import ValidationError

from edc_base.model.models import BaseUuidModel
from edc_consent.models import RequiresConsentMixin
from edc_export.models import ExportTrackingFieldsMixin
from edc_offstudy.models import OffStudyMixin
from edc_sync.models import SyncModelMixin
from edc_visit_tracking.constants import VISIT_REASON_NO_FOLLOW_UP_CHOICES, COMPLETED_PROTOCOL_VISIT, LOST_VISIT
from edc_visit_tracking.models import VisitModelMixin, PreviousVisitMixin, CaretakerFieldsMixin

from amp.choices import VISIT_REASON

from amp.models import ScreeningConsent


class SubjectVisit(OffStudyMixin, SyncModelMixin, PreviousVisitMixin,
                   RequiresConsentMixin, CaretakerFieldsMixin, VisitModelMixin,
                   ExportTrackingFieldsMixin, BaseUuidModel):

    """ Subject visit form """

    consent_model = ScreeningConsent

    off_study_model = ('amp', 'SubjectOffStudy')

#     history = AuditTrail()

    def __unicode__(self):
        return '{} {} {}'.format(self.appointment.registered_subject.subject_identifier,
                                 self.appointment.registered_subject.first_name,
                                 self.appointment.visit_definition.code)

    def save(self, *args, **kwargs):
        self.subject_identifier = self.appointment.registered_subject.subject_identifier
#         if not self.is_eligible():
#             self.reason = FAILED_ELIGIBILITY
#         self.subject_failed_eligibility()
        super(SubjectVisit, self).save(*args, **kwargs)

    def get_visit_reason_choices(self):
        return VISIT_REASON

    def is_eligible(self):
        """Returns True if participant is either eligible antenataly."""
        eligible = False
        return eligible

    def get_visit_reason_no_follow_up_choices(self):
        """ Returns the visit reasons that do not imply any data
        collection; that is, the subject is not available. """
        dct = {}
        for item in VISIT_REASON_NO_FOLLOW_UP_CHOICES:
            if item not in [COMPLETED_PROTOCOL_VISIT, LOST_VISIT]:
                dct.update({item: item})
        return dct

    class Meta:
        app_label = 'amp'
        verbose_name = 'Subject Visit'
