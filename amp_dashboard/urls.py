from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .classes import AmpDashboard

urlpatterns = []

for pattern in AmpDashboard.get_urlpatterns():
    urlpatterns.append(
        url(pattern,
            login_required(AmpDashboard.as_view()),
            name=AmpDashboard.dashboard_url_name))
