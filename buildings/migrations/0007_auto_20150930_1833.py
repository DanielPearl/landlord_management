# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0006_auto_20150930_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='image',
            field=models.ImageField(upload_to='static/images', default=None),
        ),
    ]
