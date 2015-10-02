# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0002_auto_20150929_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='tenant_image',
            field=models.ImageField(default=None, upload_to=None),
        ),
        migrations.AlterField(
            model_name='building',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
