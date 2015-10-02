# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0005_delete_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenant',
            name='tenant_image',
        ),
        migrations.AddField(
            model_name='tenant',
            name='image',
            field=models.ImageField(upload_to=None, default='static/images'),
        ),
    ]
