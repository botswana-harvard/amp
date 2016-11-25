from operator import itemgetter

from django.conf import settings
from django.contrib import admin
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from edc_base.view_mixins import EdcBaseViewMixin
from edc_label.view_mixins import EdcLabelViewMixin
from edc_visit_tracking.constants import SCHEDULED

from amp.apps import AmpAppConfig
from amp.constants import SUBJECT
from amp.models import Appointment, ScreeningConsent, SubjectVisit


class AppointmentSubjectVisitCRFViewMixin:

    paginate_by = 10

    @property
    def appointments(self):
        """Returns all appointments for this registered_subject or just one
        if given a appointment_code and appointment_continuation_count.

        Could show
            one
            all
            only for this membership form category (which is the subject type)
            only those for a given membership form
            only those for a visit definition grouping
            """
        appointments = []
        if self.appointment:
            appointments = [self.appointment]
        else:
            appointments = Appointment.objects.filter(
                subject_identifier=self.subject_identifier).order_by('visit_code')
        if appointments:
            ordered_appointments = []
            appointments_list = []
            for appointment in appointments:
                ordered_appointments.append([int(float(appointment.visit_code)), appointment])
            ordered_appointments = sorted(ordered_appointments, key=itemgetter(0))
            for _, appointment in ordered_appointments:
                appointments_list.append(appointment)
                try:
                    SubjectVisit.objects.get(appointment=appointment)
                except SubjectVisit.DoesNotExist:
                    SubjectVisit.objects.create(
                        appointment=appointment,
                        report_datetime=timezone.now(),
                        reason=SCHEDULED,
                        study_status=SCHEDULED)
        paginator = Paginator(appointments_list, self.paginate_by)
        try:
            appointments_list = paginator.page(self.kwargs.get('page', 1))
        except EmptyPage:
            appointments_list = paginator.page(paginator.num_pages)
        return appointments_list

    @property
    def appointment(self):
        appointment_id = self.context.get('appointment_pk')
        appointment = None
        try:
            appointment = Appointment.objects.get(pk=appointment_id)
        except Appointment.DoesNotExist:
            pass
        return appointment


class SubjectDashboardView(
        AppointmentSubjectVisitCRFViewMixin, EdcBaseViewMixin, EdcLabelViewMixin, TemplateView):

    def __init__(self, **kwargs):
        super(SubjectDashboardView, self).__init__(**kwargs)
        self.request = None
        self.screening_consent = None
        self.markey_next_row = 15
        self.consent_model = None
        self.context = {}
        self.template_name = 'amp_dashboard/subject_dashboard.html'
        super(EdcLabelViewMixin, self).__init__()

    def get_context_data(self, **kwargs):
        self.context = super().get_context_data(**kwargs)
        self.context.update(
            title=settings.PROJECT_TITLE,
            project_name=settings.PROJECT_TITLE,
            site_header=admin.site.site_header,
        )
        self.context.update({
            'markey_data': self.markey_data.items(),
            'markey_next_row': self.markey_next_row,
            'appointments': self.appointments,
            'subject_identifier': self.subject_identifier,
            'consents': [("Screening Consent(complete)", self.consent)],
            'dashboard_type': SUBJECT
        })
        return self.context

    def get(self, request, *args, **kwargs):
        self.request = request
        context = self.get_context_data(**kwargs)
        self.print_barcode_label(request)
        return self.render_to_response(context)

    def label_context(self, visit_code, extra_context=None):
        context = {}
        context.update({
            'dob': self.screening_consent.dob,
            'gender': self.screening_consent.gender,
            'initials': self.screening_consent.initials,
            'protocol': AmpAppConfig.protocol_number,
            'site': '12701',
            'subject_identifier': self.screening_consent.subject_identifier,
            'visit_code': visit_code,
        })
        return context

    def print_barcode_label(self, request, copies=1, context=None):
        if request:
            subject_identifier = request.GET.get('subject_identifier')
            appointment_pk = request.GET.get('appointment_pk')
            try:
                appointment = Appointment.objects.get(pk=appointment_pk)
            except Appointment.DoesNotExist:
                pass
        if subject_identifier and appointment_pk:
            self.screening_consent = ScreeningConsent.objects.get(subject_identifier=subject_identifier)
            print_value = request.GET.get('print', None)
            if print_value:
                copies = 1 if copies is None else copies
                label_template = 'amp_screeningconsent_label_template'
                context = self.label_context(appointment.visit_code)
                super(SubjectDashboardView, self).print_label(
                    label_template, copies=copies, context=context)

    @property
    def consent(self):
        try:
            screening_consent = ScreeningConsent.objects.get(subject_identifier=self.subject_identifier)
        except ScreeningConsent.DoesNotExist:
            screening_consent = None
        return screening_consent

    @property
    def subject_identifier(self):
        return self.context.get('subject_identifier')

    @property
    def markey_data(self):
        markey_data = {}
        if self.consent:
            markey_data = {
                'Name': '{}({})'.format(self.consent.first_name, self.consent.initials),
                'Born': self.consent.dob,
                'Consented': self.consent.consent_datetime,
                'Omang': self.consent.identity,
                'Gender': self.gender,
                'Age Today': self.consent.age(),
                'Identifier': self.consent.subject_identifier,
            }
        return markey_data

    @property
    def gender(self):
        gender = 'Female' if self.consent.gender == 'F' else 'Male'
        return gender

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SubjectDashboardView, self).dispatch(*args, **kwargs)
