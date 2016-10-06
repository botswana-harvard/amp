from django import forms

from edc_consent.form_mixins import ConsentFormMixin
from amp.models.screening_consent import ScreeningConsent
from .models import StudyConsent, SubjectOffStudy, SubjectRequisition, SubjectVisit

from edc_visit_tracking.form_mixins import VisitFormMixin
from edc_lab.requisition.forms import RequisitionFormMixin
from edc_offstudy.forms import OffStudyFormMixin


from amp.choices import PANELS, VISIT_REASON, VISIT_INFO_SOURCE
from edc_constants.constants import ON_STUDY
from django.contrib.admin.widgets import AdminRadioSelect, AdminRadioFieldRenderer
from amp.models.appointment import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = '__all__'


class ScreeningConsentForm(ConsentFormMixin, forms.ModelForm):

    class Meta:
        model = ScreeningConsent
        fields = '__all__'


class StudyConsentForm(ConsentFormMixin, forms.ModelForm):

    class Meta:
        model = StudyConsent
        fields = '__all__'


class SubjectOffStudyForm(OffStudyFormMixin, forms.ModelForm):

    class Meta:
        model = SubjectOffStudy
        fields = '__all__'


class SubjectRequisitionForm(RequisitionFormMixin, forms.ModelForm):
    panel_name = forms.ChoiceField(
        choices=PANELS,
        required=True,
        widget=forms.RadioSelect(),
        label="Panel"
    )

    class Meta:
        model = SubjectRequisition
        fields = '__all__'


class SubjectVisitForm(VisitFormMixin, forms.ModelForm):

    study_status = forms.ChoiceField(
        label='What is the mother\'s current study status',
        choices=VISIT_REASON,
        initial=ON_STUDY,
        help_text="",
        widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer)
    )

    reason = forms.ChoiceField(
        label='Reason for visit',
        choices=[choice for choice in VISIT_REASON],
        help_text="",
        widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer))

    info_source = forms.ChoiceField(
        label='Source of information',
        required=False,
        choices=[choice for choice in VISIT_INFO_SOURCE],
        widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer))

    dashboard_type = 'maternal'

    class Meta:
        model = SubjectVisit
        fields = '__all__'
