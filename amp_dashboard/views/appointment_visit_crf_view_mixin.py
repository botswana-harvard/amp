from django.utils import timezone

from amp.models.appointment import Appointment
from amp.models.subject_visit import SubjectVisit

from edc_visit_tracking.constants import SCHEDULED
from operator import itemgetter


class AppointmentSubjectVisitCRFViewMixin:

    def __init__(self):
        self.subject_identifier = None
        self.show = None

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
