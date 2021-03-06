from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from edc_base.view_mixins import EdcBaseViewMixin

from edc_label.view_mixins import EdcLabelViewMixin

from .forms import ScreeningConsentSearchForm
from .models.screening_consent import ScreeningConsent


class HomeView(EdcBaseViewMixin, EdcLabelViewMixin, FormView):
    template_name = 'amp/home.html'
    verbose_name = 'amp'
    form_class = ScreeningConsentSearchForm
    paginate_by = 5
    paginator_template = 'amp/paginator_row.html'
    dashboard_url_name = 'subject_dashboard_url'
    number_of_copies = 1

    def __init__(self, **kwargs):
        self.screening_consents = ScreeningConsent.objects.all(
        ).order_by('-consent_datetime')[0:15]
        paginator = Paginator(self.screening_consents, self.paginate_by)
        try:
            self.screening_consents = paginator.page(kwargs.get('page', 1))
        except EmptyPage:
            self.screening_consents = paginator.page(paginator.num_pages)
        super(HomeView, self).__init__(**kwargs)

    def get_success_url(self):
        return reverse('home_url')

    def form_valid(self, form):
        if form.is_valid():
            subject_identifier = form.cleaned_data['subject_identifier']
            try:
                self.screening_consents = ScreeningConsent.objects.filter(
                    subject_identifier__icontains=subject_identifier)
            except ScreeningConsent.DoesNotExist:
                form.add_error(
                    'subject_identifier', 'Subject not found. Please search again or add a new Screening Consent.')
            context = self.get_context_data(form=form)
            context.update({
                'screening_consents': self.screening_consents})
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        if self.kwargs.get('subject_requisition_pk'):
            self.print_label()
        context.update({'dashboard_url_name': self.dashboard_url_name})
        context.update({
            'screening_consents': self.screening_consents})
        context.update(
            title=settings.PROJECT_TITLE,
            project_name=settings.PROJECT_TITLE,
            site_header=admin.site.site_header,
        )
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)
