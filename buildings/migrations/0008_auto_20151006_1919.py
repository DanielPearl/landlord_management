# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0007_auto_20150930_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='building_id',
        ),
        migrations.AddField(
            model_name='unit',
            name='building_id',
            field=models.ManyToManyField(to='buildings.Building'),
        ),
    ]
