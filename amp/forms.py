from django import forms

from edc_consent.form_mixins import ConsentFormMixin
from amp.models.screening_consent import ScreeningConsent


class ScreeningConsentForm(ConsentFormMixin, forms.ModelForm):

    class Meta:
        model = ScreeningConsent
        fields = '__all__'
