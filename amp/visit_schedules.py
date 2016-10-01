from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from edc_visit_schedule.visit_schedule import VisitSchedule
from edc_visit_schedule.visit import Requisition
from edc_visit_schedule.schedule import Schedule
from amp_lab.lab_profiles import rdb_panel, viral_load_panel

crfs = (
)

requisitions = (
    Requisition(show_order=10, model='amp.SubjectRequisition', panel=rdb_panel),
    Requisition(show_order=20, model='amp.SubjectRequisition', panel=viral_load_panel),
)

subject_visit_schedule = VisitSchedule(
    name='subject_visit_schedule',
    verbose_name='Amp Visit Schedule',
    app_label='amp',
    visit_model='amp.subjectvisit',
)

# add schedules
schedule = Schedule(name='amp.enrollment', enrollment_model='amp.enrollment')

# add visits to this schedule
schedule.add_visit(
    code='100',
    title='Visit 100',
    timepoint=0,
    base_interval=0,
    requisitions=requisitions,
    crfs=crfs)

subject_visit_schedule.add_schedule(schedule)

# register the visit_schedule
site_visit_schedules.register(subject_visit_schedule)
