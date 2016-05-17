__author__ = 'hannahpark'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_profile, name='profile'),
    url(r'^edit_profile/', views.edit_profile, name='edit_profile'),
]