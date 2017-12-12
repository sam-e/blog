from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.budget_home, name='budget_home'),
]