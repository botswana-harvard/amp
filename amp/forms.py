from django import forms

from edc_consent.form_mixins import ConsentFormMixin
from amp.models.screening_consent import ScreeningConsent
from .models import StudyConsent, SubjectOffStudy, SubjectRequisition, SubjectVisit


class ScreeningConsentForm(ConsentFormMixin, forms.ModelForm):

    class Meta:
        model = ScreeningConsent
        fields = '__all__'


class StudyConsentForm(ConsentFormMixin, forms.ModelForm):

    class Meta:
        model = StudyConsent
        fields = '__all__'


class SubjectOffStudyForm(ConsentFormMixin, forms.ModelForm):

    class Meta:
        model = SubjectOffStudy
        fields = '__all__'


class SubjectRequisitionForm(ConsentFormMixin, forms.ModelForm):

    class Meta:
        model = SubjectRequisition
        fields = '__all__'


class SubjectVisitForm(ConsentFormMixin, forms.ModelForm):

    class Meta:
        model = SubjectVisit
        fields = '__all__'
