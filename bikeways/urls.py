from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^bikeways/$', views.route, name='route'),
    ]
