from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

from accounts import views


urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='accounts/index.html'),
        name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
        name='logout_then_login'),
    url(r'^home/$',
        login_required(TemplateView.as_view(template_name=
                                            'accounts/home.html')),
        name='home'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change',
        {'template_name': 'accounts/password_change_form.html'},
        name='password_change'),
    url(r'^password_change_done/$',
        'django.contrib.auth.views.password_change_done',
        {'template_name': 'accounts/password_change_done.html'},
        name='password_change_done'),
)
