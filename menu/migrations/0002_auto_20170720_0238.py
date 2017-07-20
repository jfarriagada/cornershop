# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 02:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='datetime',
        ),
        migrations.AddField(
            model_name='menu',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 20, 2, 38, 59, 505648)),
        ),
        migrations.AddField(
            model_name='menu',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 20, 2, 38, 59, 505690)),
        ),
    ]
