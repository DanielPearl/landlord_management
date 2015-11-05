# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0020_auto_20151103_0019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item_detail',
            name='install_duration',
        ),
    ]
