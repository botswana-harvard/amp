from django.core.paginator import Paginator, EmptyPage
from django.contrib import admin
from django.conf import settings
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from edc_label.view_mixins import EdcLabelViewMixin
from edc_base.views import EdcBaseViewMixin

from amp.forms import ScreeningConsentSearchForm
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from amp.models.screening_consent import ScreeningConsent
from amp.models.subject_requisition import SubjectRequisition


class HomeView(EdcBaseViewMixin, EdcLabelViewMixin, FormView):
    template_name = 'amp/home.html'
    form_class = ScreeningConsentSearchForm
    paginate_by = 5
    paginator_template = 'amp/paginator_row.html'
    number_of_copies = 1

    def __init__(self, **kwargs):
        self.screening_consent = None
        super(HomeView, self).__init__(**kwargs)

    def get_success_url(self):
        return reverse('home_url')

    def form_valid(self, form):
        if form.is_valid():
            subject_identifier = form.cleaned_data['subject_identifier']
            try:
                self.screening_consent = ScreeningConsent.objects.get(subject_identifier=subject_identifier)
            except ScreeningConsent.DoesNotExist:
                form.add_error('subject_identifier', 'Subject not found. Please search again or add a new Screening Consent.')
            context = self.get_context_data(form=form, subject_requisitions=self.subject_requisitions)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        subject_requisition = None
        if self.kwargs.get('subject_requisition_pk'):
            self.print_label()
        if not self.screening_consent:
            try:
                self.screening_consent = ScreeningConsent.objects.get(subject_identifier=self.kwargs.get('subject_identifier'))
                print(self.screening_consent, 'self.screening_consent')
            except ScreeningConsent.DoesNotExist:
                pass
        if self.screening_consent:
            subject_requisition = SubjectRequisition.objects.filter(subject_visit__subject_identifier=self.screening_consent.subject_identifier).order_by('subject_visit__appointment__visit_code')
        if subject_requisition:
            context.update({'subject_requisition': subject_requisition})
        context.update({
            'screening_consent': self.screening_consent})
        return context
        context.update(
            title=settings.PROJECT_TITLE,
            project_name=settings.PROJECT_TITLE,
            site_header=admin.site.site_header,
        )
        return context

    @property
    def subject_requisitions(self):
        """Returns subject_requisitions queryset after pagination."""
        subject_requisitions = []
        if self.screening_consent:
            subject_requisitions = SubjectRequisition.objects.filter(
                subject_visit__subject_identifier=self.screening_consent.subject_identifier
            ).order_by('subject_visit__appointment__visit_code')
            paginator = Paginator(subject_requisitions, self.paginate_by)
            try:
                subject_requisitions = paginator.page(self.kwargs.get('page', 1))
            except EmptyPage:
                subject_requisitions = paginator.page(paginator.num_pages)
        return subject_requisitions

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)
