# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0008_auto_20151006_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='building_id',
        ),
        migrations.AddField(
            model_name='unit',
            name='building_id',
            field=models.ForeignKey(default=1, to='buildings.Building'),
            preserve_default=False,
        ),
    ]
