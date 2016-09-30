from datetime import datetime

try:
    from config.labels import aliquot_label
except ImportError:
    aliquot_label = None

from edc.apps.app_configuration.classes import BaseAppConfiguration
from edc.core.bhp_variables.models import StudySpecific, StudySite
from edc.lab.lab_packing.models import DestinationTuple
from edc.lab.lab_profile.classes import ProfileItemTuple, ProfileTuple

from lis.labeling.classes import LabelPrinterTuple, ZplTemplateTuple, ClientTuple
from lis.specimen.lab_aliquot_list.classes import AliquotTypeTuple
from lis.specimen.lab_panel.classes import PanelTuple

study_start_datetime = datetime(2016, 07, 22, 8, 00, 00)
study_end_datetime = datetime(2016, 9, 30, 23, 49, 40)


class AppConfiguration(BaseAppConfiguration):

    def prepare(self):
        super(AppConfiguration, self).prepare()

    global_configuration = {
        'dashboard': {
            'show_not_required_metadata': False,
            'allow_additional_requisitions': False,
            'show_drop_down_requisitions': True
        },
        'appointment': {'allowed_iso_weekdays': '12345', 'use_same_weekday': True, 'default_appt_type': 'default'},
    }

    study_variables_setup = {
        'protocol_number': 'BHP086',
        'protocol_code': '086',
        'protocol_title': 'BHP086',
        'research_title': 'BHP086',
        'study_start_datetime': study_start_datetime,
        'minimum_age_of_consent': 16,
        'maximum_age_of_consent': 64,
        'gender_of_consent': 'F',
        'subject_identifier_seed': '10000',
        'subject_identifier_prefix': '086',
        'subject_identifier_modulus': '8',
        'subject_type': 'subject',
        'machine_type': 'SERVER',
        'hostname_prefix': 's007',
        'device_id': '0'}
    
    # NO CONSENT
    v1_consent_catalogue_setup = {
        'name': 'amp',
        'content_type_map': 'consent',
        'consent_type': 'study',
        'version': 1,
        'start_datetime': study_start_datetime,
        'end_datetime': study_end_datetime,
        'add_for_app': 'amp'}

    study_site_setup = [
        {'site_name': 'Gaborone', 'site_code': '4'}
    ]

    lab_clinic_api_setup = {
        'panel': [
            PanelTuple('Viral Load', 'TEST', 'WB'),
            PanelTuple('Hematology (ARV)', 'TEST', 'WB'),
            PanelTuple('PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB'),
            PanelTuple('CD4 (ARV)', 'TEST', 'WB'),
            PanelTuple('Chemistry NVP/LFT + ALPL6 (ARV)', 'TEST', 'WB'),
            PanelTuple('BHP086 Chemistry NON-LPV', 'TEST', 'WB'),
            PanelTuple('BHP086 Chemistry LPV', 'TEST', 'WB'),
            PanelTuple('DNA PCR', 'TEST', 'WB'),
            PanelTuple('ELISA', 'TEST', 'WB'),
            PanelTuple('Pharmacokinetics', 'TEST', 'WB'),
            PanelTuple('Plasma and Buffy Coat Storage', 'STORAGE', 'WB'),
            PanelTuple('HIV Genotyping', 'TEST', 'WB'),
            PanelTuple('Plasma Storage', 'STORAGE', 'WB'),
        ],
        'aliquot_type': [
            AliquotTypeTuple('Whole Blood', 'WB', '02'),
            AliquotTypeTuple('Serum', 'SERUM', '06'),
            AliquotTypeTuple('Dried Blood Spot', 'DBS', '01'),
            AliquotTypeTuple('Plasma', 'PL', '32'),
            AliquotTypeTuple('Buffy Coat', 'BC', '16'),
        ]
    }

    lab_setup = {
        'amp': {
            'destination': [DestinationTuple('BHP086', 'HPTN Reference Laboratory',
                                             'Gaborone', '3902671', 'hptn@bhp.org.bw'), ],
            'panel': [
                PanelTuple('Viral Load', 'TEST', 'WB'),
                PanelTuple('Hematology', 'TEST', 'WB'),
                PanelTuple('PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB'),
                PanelTuple('CD4 (ARV)', 'TEST', 'WB'),
                PanelTuple('Chemistry', 'TEST', 'WB'),
                PanelTuple('BHP086 Chemistry NON-LPV', 'TEST', 'WB'),
                PanelTuple('BHP086 Chemistry LPV', 'TEST', 'WB'),
                PanelTuple('DNA PCR', 'TEST', 'WB'),
                PanelTuple('HIV ELISA', 'TEST', 'WB'),
                PanelTuple('Pharmacokinetics', 'TEST', 'WB'),
                PanelTuple('Plasma and Buffy Coat Storage', 'STORAGE', 'WB'),
                PanelTuple('HIV Genotyping', 'TEST', 'WB'),
                PanelTuple('Plasma Storage', 'STORAGE', 'WB'),
                PanelTuple('Urinalysis', 'TEST', 'WB'),
                PanelTuple('HIV Diagnostics', 'TEST', 'WB'),
                PanelTuple('Viral Isolation/Sequencing', 'STORAGE', 'WB'),
                PanelTuple('VRC01 Ab levels', 'STORAGE', 'WB'),
                PanelTuple('ARV Detection', 'STORAGE', 'WB'),
                PanelTuple('Anti-VRC01 Ab levels', 'STORAGE', 'WB'),
                PanelTuple('Functional Humoral Assays', 'STORAGE', 'WB'),
                PanelTuple('Serum', 'STORAGE', 'WB'),
                PanelTuple('Host Genetics', 'STORAGE', 'WB'),
                PanelTuple('PBMC', 'STORAGE', 'WB'),
                PanelTuple('Chlamydia trachomatis/neisseria gonorrhoeae pcr', 'TEST', 'WB'),
                PanelTuple('Screening Hiv Test', 'TEST', 'WB'),
                PanelTuple('Syphillis', 'TEST', 'WB'),
            ],
            'aliquot_type': [
                AliquotTypeTuple('Whole Blood', 'WB', '02'),
                AliquotTypeTuple('Serum', 'SERUM', '06'),
                AliquotTypeTuple('Dried Blood Spot', 'DBS', '01'),
                AliquotTypeTuple('Plasma', 'PL', '32'),
                AliquotTypeTuple('Buffy Coat', 'BC', '16'),
            ],
            'profile': [ProfileTuple('PBMC Plasma (STORE ONLY)', 'WB'), ],
            'profile_item': [
                ProfileItemTuple('PBMC Plasma (STORE ONLY)', 'PL', 1.8, 3),
                ProfileItemTuple('PBMC Plasma (STORE ONLY)', 'BC', 0.5, 1),
            ]
        }}

    labeling_setup = {
        'label_printer': [
            LabelPrinterTuple('ZebraF', 'eit020', '10.113.201.??', True), ],
        'client': [
            ClientTuple(hostname='ampprinter', aliases=None, ip=None, printer_name='ZebraG', cups_hostname='eitprinter',),
        ],
        'zpl_template': [
            aliquot_label or ZplTemplateTuple(
                'aliquot_label', (
                    ('^XA\n' +
                     ('^FO320,15^A0N,16,20^FD${protocol} Site ${site} ${clinician_initials}   '
                      '${aliquot_type} ${aliquot_count}${primary}^FS\n') +
                     '^FO320,34^BY1,3.0^BCN,50,N,N,N\n'
                     '^BY^FD${aliquot_identifier}^FS\n'
                     '^FO320,92^A0N,16,20^FD${aliquot_identifier}^FS\n'
                     '^FO320,110^A0N,16,20^FD${panel} ${aliquot_type}^FS\n'
                     '^FO320,129^A0N,16,20^FD${subject_identifier} (${initials})^FS\n'
                     '^FO320,144^A0N,16,20^FDDOB: ${dob} ${gender}^FS\n'
                     '^FO320,162^A0N,16,20^FD${drawn_datetime}^FS\n'
                     '^XZ')), False),
        ],
    }

    consent_catalogue_list = [v1_consent_catalogue_setup, ]

    def update_or_create_study_variables(self):
        if StudySpecific.objects.all().count() == 0:
            StudySpecific.objects.create(**self.study_variables_setup)
        else:
            StudySpecific.objects.all().update(**self.study_variables_setup)
        self._setup_study_sites()

    def _setup_study_sites(self):
        for site in self.study_site_setup:
            try:
                StudySite.objects.get(**site)
            except StudySite.DoesNotExist:
                StudySite.objects.create(**site)
