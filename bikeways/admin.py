from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from .models import CoordinateWithID


class AdminSite(admin.ModelAdmin):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('PathFinder Admin')

    # Text to put in each page's <h1>.
    site_header = ugettext_lazy('PathFinder Administration')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('PathFinder Administration')

admin.site.register(CoordinateWithID)
