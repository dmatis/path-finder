from django.db import models

class CoordinateWithID(models.Model):
    key = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)



