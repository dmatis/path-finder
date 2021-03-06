"""Sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from registration.backends.default.views import RegistrationView
from accounts.forms import UserRegistrationForm

urlpatterns = [
    url(r'^$', 'Path_Finder_project.views.home', name='home'),
    url(r'^coordwithid_test/', 'Path_Finder_project.views.coordwithid_test'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/$', 'Path_Finder_project.views.about', name='about'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
                      {'next_page': '/'}),
    url(r'accounts/register/$',
        RegistrationView.as_view(form_class=UserRegistrationForm),
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/profile/', include('accounts.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
