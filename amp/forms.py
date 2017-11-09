from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from edc_consent.modelform_mixins import ConsentModelFormMixin
from edc_constants.constants import ON_STUDY, FEMALE
from edc_visit_tracking.modelform_mixins import VisitTrackingModelFormMixin


from .choices import VISIT_REASON, VISIT_INFO_SOURCE, GENDER_FEMALE, STUDY_SITES
from .models import Appointment, SubjectVisit, ScreeningConsent


# from django.contrib.admin.widgets import AdminRadioSelect, AdminRadioFieldRenderer
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


class ScreeningConsentForm(ConsentModelFormMixin, forms.ModelForm):

    study_site = forms.ChoiceField(
        label='Study site',
        choices=STUDY_SITES,
        initial=settings.DEFAULT_STUDY_SITE,
        help_text="")
#         widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer))

    gender = forms.ChoiceField(
        label="Gender",
        choices=GENDER_FEMALE,
        initial=FEMALE,
        widget=forms.RadioSelect())

    class Meta:
        model = ScreeningConsent
        fields = '__all__'


class SubjectVisitForm(VisitTrackingModelFormMixin, forms.ModelForm):

    study_status = forms.ChoiceField(
        label='What is the mother\'s current study status',
        choices=VISIT_REASON,
        initial=ON_STUDY,
        help_text=""
        #         widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer)
    )

    reason = forms.ChoiceField(
        label='Reason for visit',
        choices=[choice for choice in VISIT_REASON],
        help_text="")
#         widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer))

    info_source = forms.ChoiceField(
        label='Source of information',
        required=False,
        choices=[choice for choice in VISIT_INFO_SOURCE])
#         widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer))

    dashboard_type = 'maternal'

    class Meta:
        model = SubjectVisit
        fields = '__all__'
