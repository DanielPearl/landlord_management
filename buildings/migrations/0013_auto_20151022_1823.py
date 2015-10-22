# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0012_auto_20151022_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='number_of_units',
            field=models.IntegerField(default=None),
        ),
    ]
