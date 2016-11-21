from edc_visit_schedule.schedule import Schedule
from edc_visit_schedule.visit import Requisition
from edc_visit_schedule.visit_schedule import VisitSchedule

from ..lab_profiles import rdb_panel, viral_load_panel

from .requistions_entries import visits

crfs = (
)

requisitions = (
    Requisition(show_order=10, model='amp_lab.SubjectRequisition', panel=rdb_panel),
    Requisition(show_order=20, model='amp_lab.SubjectRequisition', panel=viral_load_panel),
)

subject_visit_schedule_screeningconsent = VisitSchedule(
    name='subject_visit_schedule',
    verbose_name='Amp Visit Schedule',
    app_label='amp',
    visit_model='amp.subjectvisit',
)

# add schedules
schedule_screening_consent = Schedule(name='schedule-1', enrollment_model='amp.enrollment')

# add visits to this schedule
interval = 4
for visit in visits:
    code, reqs = visit
    interval = interval + 4
    schedule_screening_consent.add_visit(
        code=code,
        title='Visit {}'.format(code),
        timepoint=interval,
        base_interval=interval,
        requisitions=reqs,
        crfs=crfs)

subject_visit_schedule_screeningconsent.add_schedule(schedule_screening_consent)
