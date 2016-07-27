from dateutil.relativedelta import relativedelta
from datetime import timedelta

from django import forms
from django.conf import settings
from django.forms.utils import ErrorList
from django.utils import timezone
from django.contrib.admin.widgets import AdminRadioSelect, AdminRadioFieldRenderer

from edc_consent.forms.base_consent_form import BaseConsentForm
from edc_constants.constants import FEMALE, OMANG, OTHER
from amp.models import ScreeningConsent


class ScreeningConsentForm(BaseConsentForm):

#     study_site = forms.ChoiceField(
#         label='Study site',
#         choices=STUDY_SITES,
#         initial=settings.DEFAULT_STUDY_SITE,
#         help_text="",
#         widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer))

    def validate_eligibility_age(self):
        #cleaned_data = self.cleaned_data
        pass
#         try:
#             identity = cleaned_data.get('identity')
#             consent_v1 = MaternalConsent.objects.get(identity=identity, version=1)
#             consent_age = relativedelta(consent_v1.consent_datetime.date(), consent_v1.dob).years
#         except MaternalConsent.DoesNotExist:
#             consent_age = relativedelta(timezone.now().date(), cleaned_data.get('dob')).years
#         eligibility_age = MaternalEligibility.objects.get(
#             registered_subject=cleaned_data.get('registered_subject')).age_in_years
#         if consent_age != eligibility_age:
#             raise forms.ValidationError(
#                 'In Maternal Eligibility you indicated the participant is {}, '
#                 'but age derived from the DOB is {}.'.format(eligibility_age, consent_age))

#     def validate_recruit_source(self):
#         cleaned_data = self.cleaned_data
#         if cleaned_data.get('recruit_source') == OTHER:
#             if not cleaned_data.get('recruit_source_other'):
#                 self._errors["recruit_source_other"] = ErrorList(["Please specify how you first learnt about the study."
#                                                                   ])
#                 raise forms.ValidationError('You indicated that mother first learnt about the study from a source other'
#                                             ' than those in the list provided. Please specify source.')
#         else:
#             if cleaned_data.get('recruit_source_other'):
#                 self._errors["recruit_source_other"] = ErrorList(["Please do not specify source you first learnt about"
#                                                                   " the study from."])
#                 raise forms.ValidationError('You CANNOT specify other source that mother learnt about the study from '
#                                             'as you already indicated {}'.format(cleaned_data.get('recruit_source')))

    def validate_recruitment_clinic(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('recruitment_clinic') == OTHER:
            if not cleaned_data.get('recruitment_clinic_other'):
                self._errors["recruitment_clinic_other"] = ErrorList(["Please specify health facility."])
                raise forms.ValidationError('You indicated that mother was recruited from a health facility other '
                                            'than that list provided. Please specify that health facility.')
        else:
            if cleaned_data.get('recruitment_clinic_other'):
                self._errors["recruitment_clinic_other"] = ErrorList(["Please do not specify health facility."])
                raise forms.ValidationError('You CANNOT specify other facility that mother was recruited from as you '
                                            'already indicated {}'.format(cleaned_data.get('recruitment_clinic')))

    class Meta:
        model = ScreeningConsent
        fields = '__all__'
