# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0013_auto_20151022_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_detail',
            name='cost',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='item_detail',
            name='install_duration',
            field=models.DurationField(),
        ),
    ]
