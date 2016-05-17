# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikeways', '0002_auto_20151025_0044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coordinatedata',
            old_name='coordinate',
            new_name='lat',
        ),
        migrations.AddField(
            model_name='coordinatedata',
            name='lng',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
