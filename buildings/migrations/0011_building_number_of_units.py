# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0010_auto_20151016_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='number_of_units',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
