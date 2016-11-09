from django import forms
from django.conf import settings

from edc_consent.form_mixins import ConsentFormMixin
from amp.models.screening_consent import ScreeningConsent
from .models import SubjectOffStudy, SubjectRequisition, SubjectVisit

from edc_visit_tracking.form_mixins import VisitFormMixin
from edc_lab.requisition.forms import RequisitionFormMixin
from edc_offstudy.forms import OffStudyFormMixin


from amp.choices import PANELS, VISIT_REASON, VISIT_INFO_SOURCE, GENDER_FEMALE
from edc_constants.constants import ON_STUDY, FEMALE
from django.contrib.admin.widgets import AdminRadioSelect, AdminRadioFieldRenderer
from amp.models.appointment import Appointment

from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django.core.urlresolvers import reverse

from amp.choices import STUDY_SITES


class ScreeningConsentSearchForm(forms.Form):

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        max_length=36)

    def __init__(self, *args, **kwargs):
        super(ScreeningConsentSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper = FormHelper()
        self.helper.form_action = reverse('home_url')
        self.helper.form_id = 'form-subject-search'
        self.helper.form_method = 'post'
        self.helper.html5_required = True
        self.helper.layout = Layout(
            FieldWithButtons('subject_identifier', StrictButton('Search', type='submit')))


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = '__all__'


class ScreeningConsentForm(ConsentFormMixin, forms.ModelForm):

    study_site = forms.ChoiceField(
        label='Study site',
        choices=STUDY_SITES,
        initial=settings.DEFAULT_STUDY_SITE,
        help_text="",
        widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer))

    gender = forms.ChoiceField(
        label="Gender",
        choices=GENDER_FEMALE,
        initial=FEMALE,
        widget=forms.RadioSelect())

    class Meta:
        model = ScreeningConsent
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
