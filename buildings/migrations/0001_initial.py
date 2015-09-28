# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('street_number', models.IntegerField()),
                ('street_name', models.CharField(max_length=30)),
                ('unit_number', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zip_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('building_name', models.CharField(max_length=30)),
                ('occupancy', models.IntegerField()),
                ('build_date', models.DateField()),
                ('address_id', models.ForeignKey(to='buildings.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('item_description', models.TextField(null='')),
            ],
        ),
        migrations.CreateModel(
            name='Item_update',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('date', models.DateField()),
                ('cost', models.FloatField()),
                ('install_duration', models.IntegerField()),
                ('item_id', models.ForeignKey(to='buildings.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Management_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('manager_name', models.CharField(max_length=30)),
                ('start_date', models.DateField()),
                ('phone_number', models.IntegerField()),
                ('email', models.CharField(max_length=30)),
                ('address_id', models.ForeignKey(to='buildings.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tenants',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('tenant_names', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('move_in', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('unit_number', models.CharField(max_length=30)),
                ('parking_space', models.CharField(max_length=30)),
                ('building_id', models.ForeignKey(to='buildings.Building')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone_number', models.IntegerField()),
                ('email', models.CharField(max_length=30)),
                ('website', models.CharField(max_length=30)),
                ('contact_person', models.CharField(max_length=30)),
                ('address_id', models.ForeignKey(to='buildings.Address')),
            ],
        ),
        migrations.AddField(
            model_name='tenants',
            name='unit_id',
            field=models.ForeignKey(to='buildings.Unit'),
        ),
        migrations.AddField(
            model_name='room',
            name='unit_id',
            field=models.ForeignKey(to='buildings.Unit'),
        ),
        migrations.AddField(
            model_name='item_update',
            name='vendor_info',
            field=models.ForeignKey(to='buildings.Vendor'),
        ),
        migrations.AddField(
            model_name='item',
            name='room_id',
            field=models.ForeignKey(to='buildings.Room'),
        ),
        migrations.AddField(
            model_name='building',
            name='manager_id',
            field=models.ForeignKey(to='buildings.Management_info'),
        ),
    ]
