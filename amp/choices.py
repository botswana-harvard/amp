from edc_constants.constants import (
    OTHER, UNSCHEDULED, SCHEDULED, MISSED_VISIT, LOST_VISIT,
    OFF_STUDY, ON_STUDY, COMPLETED_PROTOCOL_VISIT, FAILED_ELIGIBILITY, PARTICIPANT)


STUDY_SITES = (
    ('40', 'Gaborone'),
)

VISIT_INFO_SOURCE = [
    (PARTICIPANT, 'Clinic visit with participant'),
    ('other_contact', 'Other contact with participant (for example telephone call)'),
    ('other_doctor', 'Contact with external health care provider/medical doctor'),
    ('family', 'Contact with family or designated person who can provide information'),
    ('chart', 'Hospital chart or other medical record'),
    (OTHER, 'Other')]

VISIT_REASON = [
    (SCHEDULED, 'Scheduled visit/contact'),
    (MISSED_VISIT, 'Missed Scheduled visit'),
    (UNSCHEDULED, 'Unscheduled visit at which lab samples or data are being submitted'),
    (LOST_VISIT, 'Lost to follow-up (use only when taking subject off study)'),
    (FAILED_ELIGIBILITY, 'Subject failed enrollment eligibility'),
    (COMPLETED_PROTOCOL_VISIT, 'Subject has completed the study')]

VISIT_UNSCHEDULED_REASON = (
    ('Routine oncology', 'Routine oncology clinic visit'),
    ('Ill oncology', 'Ill oncology clinic visit'),
    ('Patient called', 'Patient called to come for visit'),
    (OTHER, 'Other, specify:'),
)

VISIT_STUDY_STATUS = (
    (ON_STUDY, 'On study'),
    (OFF_STUDY, 'Off study-no further follow-up (including death); use only for last study contact'),
)
