
from edc_visit_schedule.visit import Requisition

from amp.lab_profiles import (
    hiv_diagnostics_panel, vl_iso_seq_panel, serum_panel, hema_panel, syphillis_panel,
    chem_panel, pbmc_panel, dna_pcr_panel, hema_arv_panel, urina_panel, hiv_genotyping_panel, func_homoral_panel)


requisitions_hvs = (
    Requisition(show_order=10, model='amp.SubjectRequisition', panel=hiv_diagnostics_panel),
    Requisition(show_order=20, model='amp.SubjectRequisition', panel=vl_iso_seq_panel),
    Requisition(show_order=30, model='amp.SubjectRequisition', panel=serum_panel),
)

visit_1_requisitions = (
    Requisition(show_order=10, model='amp.SubjectRequisition', panel=dna_pcr_panel),
    Requisition(show_order=20, model='amp.SubjectRequisition', panel=hema_arv_panel),
    Requisition(show_order=30, model='amp.SubjectRequisition', panel=chem_panel),
    Requisition(show_order=40, model='amp.SubjectRequisition', panel=vl_iso_seq_panel),
    Requisition(show_order=50, model='amp.SubjectRequisition', panel=urina_panel),
)

visit_2_requisitions = (
    Requisition(show_order=10, model='amp.SubjectRequisition', panel=syphillis_panel),
    Requisition(show_order=20, model='amp.SubjectRequisition', panel=chem_panel),
    Requisition(show_order=30, model='amp.SubjectRequisition', panel=hema_arv_panel),
    Requisition(show_order=40, model='amp.SubjectRequisition', panel=hiv_genotyping_panel),
    Requisition(show_order=50, model='amp.SubjectRequisition', panel=vl_iso_seq_panel),
    Requisition(show_order=60, model='amp.SubjectRequisition', panel=func_homoral_panel),
    Requisition(show_order=70, model='amp.SubjectRequisition', panel=serum_panel),
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
    ('1.0', visit_1_requisitions), ('1.1', visit_1_requisitions), ('1.2', visit_1_requisitions), ('1.3', visit_1_requisitions),
    ('2.0', visit_2_requisitions), ('2.1', visit_2_requisitions), ('2.2', visit_2_requisitions), ('2.3', visit_2_requisitions),
    ('3.0', requisitions_hvs), ('3.1', requisitions_hvs), ('3.2', requisitions_hvs), ('3.3', requisitions_hvs),
    ('4.0', requisitions_hvs), ('4.1', requisitions_hvs), ('4.2', requisitions_hvs), ('4.3', requisitions_hvs),
    ('5.0', requisitions_hvs), ('5.1', requisitions_hvs), ('5.2', requisitions_hvs), ('5.3', requisitions_hvs),
    ('6.0', visit_1600_requisitions), ('6.1', visit_1600_requisitions), ('6.2', visit_1600_requisitions), ('6.3', visit_1600_requisitions),
    ('7.0', requisitions_hvs), ('7.1', requisitions_hvs), ('7.2', requisitions_hvs), ('7.3', requisitions_hvs),
    ('8.0', requisitions_hvs), ('8.1', requisitions_hvs), ('8.2', requisitions_hvs), ('8.3', requisitions_hvs),
    ('9.0', requisitions_hvs), ('9.1', requisitions_hvs), ('9.2', requisitions_hvs), ('9.3', requisitions_hvs),
    ('10.0', requisitions_hvs), ('10.1', requisitions_hvs), ('10.2', requisitions_hvs), ('10.3', requisitions_hvs),
    ('11.0', requisitions_hvs), ('11.1', requisitions_hvs), ('11.2', requisitions_hvs), ('11.3', requisitions_hvs),
    ('12.0', requisitions_hvs), ('12.1', requisitions_hvs), ('12.2', requisitions_hvs), ('12.3', requisitions_hvs),
    ('13.0', requisitions_hvs), ('13.1', requisitions_hvs), ('13.2', requisitions_hvs), ('13.3', requisitions_hvs),
    ('14.0', visit_4800_requisitions), ('14.1', visit_4800_requisitions), ('14.2', visit_4800_requisitions), ('14.3', visit_4800_requisitions),
    ('15.0', requisitions_hvs), ('15.1', requisitions_hvs), ('15.2', requisitions_hvs), ('15.3', requisitions_hvs),
    ('16.0', requisitions_hvs), ('16.1', requisitions_hvs), ('16.2', requisitions_hvs), ('16.3', requisitions_hvs),
    ('17.0', requisitions_hvs), ('17.1', requisitions_hvs), ('17.2', requisitions_hvs), ('17.3', requisitions_hvs),
    ('18.0', requisitions_hvs), ('18.1', requisitions_hvs), ('18.2', requisitions_hvs), ('18.3', requisitions_hvs),
    ('19.0', requisitions_hvs), ('19.1', requisitions_hvs), ('19.2', requisitions_hvs), ('19.3', requisitions_hvs),
    ('20.0', requisitions_hvs), ('20.1', requisitions_hvs), ('20.2', requisitions_hvs), ('20.3', requisitions_hvs),
    ('21.0', requisitions_hvs), ('21.1', requisitions_hvs), ('21.2', requisitions_hvs), ('21.3', requisitions_hvs),
    ('22.0', requisitions_hvs), ('22.1', requisitions_hvs), ('22.2', requisitions_hvs), ('22.3', requisitions_hvs),
    ('23.0', requisitions_hvs), ('23.1', requisitions_hvs), ('23.2', requisitions_hvs), ('23.3', requisitions_hvs),
    ('24.0', requisitions_hvs), ('24.1', requisitions_hvs), ('24.2', requisitions_hvs), ('24.3', requisitions_hvs),
    ('25.0', visit_9200_requisitions), ('25.1', visit_9200_requisitions), ('25.2', visit_9200_requisitions), ('25.3', visit_9200_requisitions)]
