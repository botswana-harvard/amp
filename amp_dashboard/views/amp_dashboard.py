from ..classes import AmpDashboard
from django.views.generic.base import TemplateView


class AmpDashboard(TemplateView):

    template_name = 'amp_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = self.amp_dashboard(context)
        return context

    def amp_dashboard(self, context):
        dashboard = AmpDashboard(
            dashboard_type=context.get('dashboard_type'),
            dashboard_id=context.get('dashboard_id'),
            dashboard_model=context.get('dashboard_model'),
            dashboard_category=context.get('dashboard_category'),
            registered_subject=context.get('registered_subject'),
            #dashboard_type_list=[INFANT],
            show=context.get('show'),
        )
        dashboard.set_context()
        return dashboard.context.get()

#
# @login_required
# def infant_dashboard(request, **kwargs):
#     dashboard = InfantDashboard(
#         dashboard_type=kwargs.get('dashboard_type'),
#         dashboard_id=kwargs.get('dashboard_id'),
#         dashboard_model=kwargs.get('dashboard_model'),
#         dashboard_category=kwargs.get('dashboard_category'),
#         registered_subject=kwargs.get('registered_subject'),
#         dashboard_type_list=[INFANT],
#         show=kwargs.get('show'),
#     )
# 
#     dashboard.set_context()
#     return render_to_response(
#         'infant_dashboard.html',
#         dashboard.context.get(),
#         context_instance=RequestContext(request))
