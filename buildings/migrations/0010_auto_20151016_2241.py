# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0009_auto_20151006_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='build_date',
            field=models.DateField(blank=True),
        ),
    ]
