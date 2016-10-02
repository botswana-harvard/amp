
from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from edc_visit_schedule.visit_schedule import VisitSchedule
from edc_visit_schedule.visit import Requisition
from edc_visit_schedule.schedule import Schedule

from amp_lab.lab_profiles import (
    hiv_diagnostics_panel, vl_iso_seq_panel, serum_panel, hema_panel, rdb_panel, viral_load_panel, syphillis_panel,
    chem_panel, pbmc_panel)


requisitions_hvs = (
    Requisition(show_order=10, model='amp.SubjectRequisition', panel=hiv_diagnostics_panel),
    Requisition(show_order=20, model='amp.SubjectRequisition', panel=vl_iso_seq_panel),
    Requisition(show_order=30, model='amp.SubjectRequisition', panel=serum_panel),
)

visit_100_requisitions = (
    Requisition(show_order=10, model='amp.SubjectRequisition', panel=rdb_panel),
    Requisition(show_order=20, model='amp.SubjectRequisition', panel=viral_load_panel),
)

visit_200_requisitions = (
    Requisition(show_order=10, model='amp.SubjectRequisition', panel=hiv_diagnostics_panel),
    Requisition(show_order=20, model='amp.SubjectRequisition', panel=hema_panel),
    Requisition(show_order=30, model='amp.SubjectRequisition', panel=syphillis_panel),
    Requisition(show_order=40, model='amp.SubjectRequisition', panel=vl_iso_seq_panel),
)

visit_1600_requisitions = (
    Requisition(show_order=10, model='amp.SubjectRequisition', panel=hiv_diagnostics_panel),
    Requisition(show_order=20, model='amp.SubjectRequisition', panel=hema_panel),
    Requisition(show_order=30, model='amp.SubjectRequisition', panel=chem_panel),
    Requisition(show_order=40, model='amp.SubjectRequisition', panel=vl_iso_seq_panel),
    Requisition(show_order=50, model='amp.SubjectRequisition', panel=serum_panel),
)

visit_4800_requisitions = (
    Requisition(show_order=10, model='amp.SubjectRequisition', panel=hiv_diagnostics_panel),
    Requisition(show_order=30, model='amp.SubjectRequisition', panel=vl_iso_seq_panel),
    Requisition(show_order=20, model='amp.SubjectRequisition', panel=syphillis_panel),
    Requisition(show_order=40, model='amp.SubjectRequisition', panel=serum_panel),
)

visit_9200_requisitions = (
    Requisition(show_order=10, model='amp.SubjectRequisition', panel=hiv_diagnostics_panel),
    Requisition(show_order=20, model='amp.SubjectRequisition', panel=vl_iso_seq_panel),
    Requisition(show_order=30, model='amp.SubjectRequisition', panel=serum_panel),
    Requisition(show_order=40, model='amp.SubjectRequisition', panel=pbmc_panel),
)

visits = [
    ('100', visit_100_requisitions), ('200', visit_200_requisitions), ('400', requisitions_hvs),
    ('800', requisitions_hvs), ('1200', requisitions_hvs), ('1600', visit_1600_requisitions),
    ('2000', requisitions_hvs), ('2400', requisitions_hvs), ('2800', requisitions_hvs),
    ('3200', requisitions_hvs), ('3600', requisitions_hvs), ('4000', requisitions_hvs),
    ('4400', requisitions_hvs), ('4800', visit_4800_requisitions), ('5200', requisitions_hvs),
    ('5600', requisitions_hvs), ('6000', requisitions_hvs), ('6400', requisitions_hvs),
    ('6800', requisitions_hvs), ('7200', requisitions_hvs), ('7600', requisitions_hvs),
    ('8000', requisitions_hvs), ('8400', requisitions_hvs), ('8800', requisitions_hvs),
    ('9200', visit_9200_requisitions)]
