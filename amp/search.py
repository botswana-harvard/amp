from django.db.models import Q

from edc_dashboard.search import BaseSearchByWord

from amp.models import ScreeningConsent


class ScreeningConsentSearchByWord(BaseSearchByWord):

    name = 'word'
    search_model = ScreeningConsent
    order_by = ['-created']
    template = 'screeningconsent_include.html'

    @property
    def qset(self):
        qset = (
            Q(subject_identifier__icontains=self.search_value) |
            Q(first_name__icontains=self.search_value))
        return qset

