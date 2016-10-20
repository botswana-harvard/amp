"""amp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from edc_base.views import LoginView, LogoutView
from .views import HomeView
from amp.admin_site import amp_admin

urlpatterns = [
    url(r'login', LoginView.as_view(), name='login_url'),
    url(r'logout', LogoutView.as_view(pattern_name='login_url'), name='logout_url'),
    url(r'^admin/', amp_admin.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^home/', HomeView.as_view(), name='home_url'),
    url(r'^amp_dashboard/', include('amp_dashboard.urls')),
    url(r'^(?P<subject_identifier>[-\w]+)/(?P<page>\d+)/$', HomeView.as_view(), name='home_url'),
    url(r'^(?P<subject_identifier>[-\w]+)/$', HomeView.as_view(), name='home_url'),
    url(r'^', HomeView.as_view(), name='home_url'),
    url(r'', include('edc_base.urls', 'edc-base')),
]
