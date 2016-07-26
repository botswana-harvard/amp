from collections import namedtuple

from edc_dashboard.section import BaseSectionView, site_sections

from .search_by_word import ScreeningConsentSearchByWord
from .models import ScreeningConsent

ModelMeta = namedtuple('ModelMeta', 'app_label model_name')


class SectionAdministrationView(BaseSectionView):
    section_name = 'administration'
    section_display_name = 'Administration'
    section_display_index = 140
    section_template = 'amp_section_admin.html'

    def contribute_to_context(self, context, request, *args, **kwargs):
        context.update({
            #'maternal_meta': ModelMeta('amp', 'maternal_eligibility'),
            'aliquot_type_meta': ModelMeta('amp_lab', 'aliquot_type'),
            'aliquot_meta': ModelMeta('amp_lab', 'aliquot'),
        })

site_sections.register(SectionAdministrationView, replaces='administration')


class SectionScreeningConsentView(BaseSectionView):
    section_name = 'screeningcosent'
    section_display_name = 'subjects'
    section_display_index = 10
    section_template = 'section_screening.html'
    dashboard_url_name = 'subject_dashboard_url'
    add_model = ScreeningConsent
    search = {'word': ScreeningConsentSearchByWord}
    show_most_recent = True

site_sections.register(SectionScreeningConsentView)
