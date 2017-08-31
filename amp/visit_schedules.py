from edc_visit_schedule.constants import WEEKS
from edc_visit_schedule.schedule import Schedule
from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from edc_visit_schedule.visit_schedule import VisitSchedule


crfs = ()

requisitions = ()

subject_visit_schedule = VisitSchedule(
    name='subject_visit_schedule',
    app_label='amp',
    default_enrollment_model='amp.enrollment',
    default_disenrollment_model='amp.disenrollment',
    visit_model='amp.subjectvisit',
    offstudy_model='amp.subjectoffstudy',
    verbose_name='Amp Visit Schedule',
)


visit_codes = [
    '1.0', '2.0', '3.0', '4.0', '5.0', '6.0', '7.0', '8.0',
    '9.0', '10.0', '11.0', '12.0', '13.0', '14.0', '15.0',
    '16.0', '17.0', '19.0', '20.0', '21.0', '22.0', '23.0',
    '24.0', '25.0', '26.0', '31.0', '32.0', '33.0', '34.0',
    '35.0', '47.0', '48.0', '71.0', '72.0', '73.0', '74.0',
    '75.0', '76.0', '77.0', '78.0']

schedule = Schedule(name='amp-schedule')
interval = 0

for code in visit_codes:
    # add visits to this schedule
    schedule.add_visit(
        code=code,
        title='Visit' + code,
        timepoint=interval,
        base_interval=interval,
        base_interval_unit=WEEKS,
        requisitions=requisitions,
        crfs=crfs)
    interval = interval + 4

subject_visit_schedule.add_schedule(schedule)

# register the visit_schedule
site_visit_schedules.register(subject_visit_schedule)
