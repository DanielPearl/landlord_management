# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0004_auto_20150930_1711'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
    ]
