# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-21 21:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_rental', '0002_ride_ride_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='Ride_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 21, 21, 39, 0, 483272)),
        ),
    ]
