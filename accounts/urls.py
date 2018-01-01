from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.register, name='register'),
    url(r'^login/$', login, {'template_name': 'home/login_base.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'home/logout_page.html'}, name='logout'),
]
