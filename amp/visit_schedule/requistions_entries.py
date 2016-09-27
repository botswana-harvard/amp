from edc_visit_schedule.classes.visit_schedule_configuration import RequisitionPanelTuple
from edc_constants.constants import NOT_REQUIRED, REQUIRED, ADDITIONAL, NOT_ADDITIONAL

visit_100_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'Screening Hiv Test', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Hematology', 'TEST', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Chemistry', 'TEST', 'WB', REQUIRED, ADDITIONAL),
)

visit_200_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Hematology', 'TEST', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Syphillis', 'TEST', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        40, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)

visit_400_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)

visit_800_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Hematology', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        40, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        50, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)

visit_1200_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)

visit_1600_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Hematology', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        40, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        50, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)

visit_2000_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        40, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        50, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)

visit_2400_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Hematology', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        40, 'amp_lab', 'subjectrequisition',
        'Syphillis', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        50, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        60, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)

visit_2800_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        50, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        60, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)

visit_3200_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Hematology', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        40, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        50, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)

visit_3600_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)

visit_4000_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Hematology', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        40, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        50, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)

visit_4400_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)

visit_4800_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Hematology', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        40, 'amp_lab', 'subjectrequisition',
        'Syphillis', 'TEST', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        50, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        60, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)

visit_5200_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)

visit_5600_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Hematology', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        40, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        50, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)


visit_6000_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)

visit_6400_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Hematology', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        40, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        50, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)

visit_6800_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)

visit_7200_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Hematology', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        40, 'amp_lab', 'subjectrequisition',
        'Syphillis', 'TEST', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        50, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        60, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)

visit_7600_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)

visit_8000_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)

visit_8400_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)

visit_8800_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)

visit_9200_requisition = (
    RequisitionPanelTuple(
        10, 'amp_lab', 'subjectrequisition',
        'HIV Diagnostics', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, 'amp_lab', 'subjectrequisition',
        'Viral Isolation/Sequencing', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        30, 'amp_lab', 'subjectrequisition',
        'Serum', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
    RequisitionPanelTuple(
        40, 'amp_lab', 'subjectrequisition',
        'PBMC', 'STORAGE', 'WB', REQUIRED, ADDITIONAL),
)
