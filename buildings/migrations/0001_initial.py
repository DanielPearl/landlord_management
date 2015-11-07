# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('street_number', models.IntegerField()),
                ('street_name', models.CharField(max_length=30)),
                ('unit_number', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=20)),
                ('zip_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('building_name', models.CharField(max_length=30)),
                ('build_date', models.DateField(blank=True)),
                ('number_of_units', models.IntegerField(default=None)),
                ('address_id', models.ForeignKey(to='buildings.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('item_description', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Item_Detail',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('vendor', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('item_id', models.ForeignKey(to='buildings.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('phone_number', models.IntegerField(default=None)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('room_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('tenant_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='static/images', default=None)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('move_in', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('unit_number', models.CharField(max_length=30)),
                ('parking_space', models.CharField(max_length=30)),
                ('is_rented', models.BooleanField(default=False)),
                ('building_id', models.ForeignKey(to='buildings.Building')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=30)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=30)),
                ('website', models.CharField(max_length=30)),
                ('contact_person', models.CharField(max_length=30)),
                ('address_id', models.OneToOneField(to='buildings.Address')),
            ],
        ),
        migrations.AddField(
            model_name='tenant',
            name='unit_id',
            field=models.ForeignKey(to='buildings.Unit'),
        ),
        migrations.AddField(
            model_name='room',
            name='unit_id',
            field=models.ForeignKey(to='buildings.Unit'),
        ),
        migrations.AddField(
            model_name='item',
            name='room_id',
            field=models.ForeignKey(to='buildings.Room'),
        ),
        migrations.AddField(
            model_name='building',
            name='manager_id',
            field=models.ManyToManyField(to='buildings.Manager'),
        ),
    ]
