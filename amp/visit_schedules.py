from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedule import schedule1

app_label = 'amp'

visit_schedule1 = VisitSchedule(
    name='visit_schedule1',
    verbose_name='Amp',
    app_label='amp',
    visit_model=f'{app_label}.subjectvisit',
    offstudy_model=f'{app_label}.subjectoffstudy',
    previous_visit_schedule=None)

visit_schedule1.add_schedule(schedule1)

site_visit_schedules.register(visit_schedule1)
