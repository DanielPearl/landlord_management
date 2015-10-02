# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buildings', '0003_auto_20150930_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='occupancy',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='address_id',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='email',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='manager_name',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='username',
        ),
        migrations.AddField(
            model_name='manager',
            name='user',
            field=models.OneToOneField(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unit',
            name='is_rented',
            field=models.BooleanField(default=False),
        ),
    ]
