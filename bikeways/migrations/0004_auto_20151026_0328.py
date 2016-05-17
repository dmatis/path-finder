# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikeways', '0003_auto_20151026_0319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coordinatedata',
            old_name='lat',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='coordinatedata',
            old_name='lng',
            new_name='longitude',
        ),
    ]
