# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 14:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('device_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=0)),
                ('pin_no', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Room'),
        ),
    ]
