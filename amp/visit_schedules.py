from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from amp.visit_schedule.screening_consent import subject_visit_schedule_screeningconsent

# from amp.visit_schedule.study_consent import subject_visit_schedule_studyconsent

# register the visit_schedule subject_visit_schedule_screeningconsent
site_visit_schedules.register(subject_visit_schedule_screeningconsent)
# register the visit_schedule subject_visit_schedule_studyconsent
# site_visit_schedules.register(subject_visit_schedule_studyconsent)
