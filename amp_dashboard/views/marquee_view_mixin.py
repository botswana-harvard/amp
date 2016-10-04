from amp.models.screening_consent import ScreeningConsent
from amp.factories import ScreeningConsentFactory
from amp.models.subject_identifier import SubjectIdentifier


class MarqueeViewMixin:

    def __init__(self):
        self.context = {}
        self.markey_next_row = 15
        self.consent_model = None

    def get_context_data(self, **kwargs):
        self.context = super(MarqueeViewMixin, self).get_context_data(**kwargs)
        return self.context

    @property
    def markey_data(self):
        markey_data = {}
        if self.consent:
            markey_data = {
                'Name': '{}({})'.format(self.consent.first_name, self.consent.initials),
                'Born': self.consent.dob,
                'Age': self.age,
                'Consented': self.consent.consent_datetime,
                'Omang': self.consent.identity,
                'Gender': self.gender,
                'Age Tody': self.age_today,
                'Identifier': self.consent.subject_identifier,
            }
        return markey_data

    def create_subject_identifiers(self):
        for identifier in ['1001243-1', '1001243-2', '1001243-3', '1001243-4', '1001243-5']:
                try:
                    SubjectIdentifier.objects.get(subject_identifier=identifier)
                except SubjectIdentifier.DoesNotExist:
                    SubjectIdentifier.objects.create(
                        subject_identifier=identifier
                    )

    @property
    def consent(self):
        self.create_subject_identifiers()
        if not ScreeningConsent.objects.filter(subject_identifier='1001243-1'):
            self.consent_model = ScreeningConsentFactory()
        return self.consent_model

    @property
    def age(self):
        return None

    @property
    def age_today(self):
        return None

    @property
    def gender(self):
        gender = 'Female' if self.consent.gender == 'F' else 'Male'
        return gender
