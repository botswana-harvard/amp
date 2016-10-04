from django.contrib.auth.decorators import login_required
from ..classes import AmpDashboard
# from django.views.generic.base import TemplateView

from amp.constants import SUBJECT
from django.shortcuts import render_to_response
from django.template.context import RequestContext


@login_required
def amp_dashboard(request, **kwargs):
    dashboard = AmpDashboard(
        dashboard_type=kwargs.get('dashboard_type'),
        dashboard_id=kwargs.get('dashboard_id'),
        dashboard_model=kwargs.get('dashboard_model'),
        dashboard_category=kwargs.get('dashboard_category'),
        registered_subject=kwargs.get('registered_subject'),
        dashboard_type_list=[SUBJECT],
        show=kwargs.get('show'),
    )
    print("amp_dashboard amp_dashboard amp_dashboard")
    return render_to_response(
        'amp_dashboard.html',
        dashboard.context.get(),
        context_instance=RequestContext(request))

# class AmpDashboard(TemplateView):
# 
#     template_name = 'amp_dashboard.html'
# 
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context = self.amp_dashboard(context)
#         return context
# 
#     def amp_dashboard(self, context):
#         dashboard = AmpDashboard(
#             dashboard_type=context.get('dashboard_type'),
#             dashboard_id=context.get('dashboard_id'),
#             dashboard_model=context.get('dashboard_model'),
#             dashboard_category=context.get('dashboard_category'),
#             #registered_subject=context.get('registered_subject'),
#             dashboard_type_list=[SUBJECT],
#             show=context.get('show'),
#         )
#         dashboard.set_context()
#         return dashboard.context.get()
