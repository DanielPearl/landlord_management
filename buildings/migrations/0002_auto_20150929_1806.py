# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date', models.DateField()),
                ('cost', models.FloatField()),
                ('install_duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('manager_name', models.CharField(max_length=30)),
                ('start_date', models.DateField()),
                ('phone_number', models.IntegerField()),
                ('email', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('tenant_name', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('move_in', models.DateField()),
                ('unit_id', models.ForeignKey(to='buildings.Unit')),
            ],
        ),
        migrations.RemoveField(
            model_name='item_update',
            name='item_id',
        ),
        migrations.RemoveField(
            model_name='item_update',
            name='vendor_info',
        ),
        migrations.RemoveField(
            model_name='management_info',
            name='address_id',
        ),
        migrations.RemoveField(
            model_name='tenants',
            name='unit_id',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='name',
            new_name='room_name',
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='name',
            new_name='vendor_name',
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='address',
            name='unit_number',
            field=models.CharField(max_length=10),
        ),
        migrations.RemoveField(
            model_name='building',
            name='manager_id',
        ),
        migrations.AlterField(
            model_name='item',
            name='item_description',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='address_id',
            field=models.OneToOneField(to='buildings.Address'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='email',
            field=models.EmailField(max_length=30),
        ),
        migrations.DeleteModel(
            name='Item_update',
        ),
        migrations.DeleteModel(
            name='Management_info',
        ),
        migrations.DeleteModel(
            name='Tenants',
        ),
        migrations.AddField(
            model_name='manager',
            name='address_id',
            field=models.OneToOneField(to='buildings.Address'),
        ),
        migrations.AddField(
            model_name='item_detail',
            name='item_id',
            field=models.ManyToManyField(to='buildings.Item'),
        ),
        migrations.AddField(
            model_name='item_detail',
            name='vendor_info',
            field=models.ForeignKey(to='buildings.Vendor'),
        ),
        migrations.AddField(
            model_name='building',
            name='manager_id',
            field=models.ManyToManyField(to='buildings.Manager'),
        ),
    ]
