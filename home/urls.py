from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^about/', views.about, name='about'),
    url(r'^login/$', login, {'template_name': 'home/home_page.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'home/logout_page.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
]
