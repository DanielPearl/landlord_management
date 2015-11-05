# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0014_auto_20151102_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_detail',
            name='install_duration',
            field=models.FloatField(),
        ),
    ]
