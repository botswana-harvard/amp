from amp.models.appointment import Appointment


class AppointmentSubjectVisitCRFViewMixin:

    def __init__(self):
        self.request = None
        self.subject_identifier

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
        if self.show == 'forms':
            appointments = [self.appointment]
        else:
            # or filter appointments for the current membership categories
            # schedule_group__membership_form
            appointments = Appointment.objects.filter(
                subject_identifier=self.subject_identifier).order_by('visit_instance', 'appt_datetime')
        return appointments

    @property
    def appointment(self):
        appointment_id = self.request.Get.get('appointment_id', None)
        appointment = None
        try:
            appointment = Appointment.objects.get(pk=appointment_id)
        except Appointment.DoesNotExist:
            pass
        return appointment