# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-31 11:41
from __future__ import unicode_literals

import django.contrib.postgres.fields.ranges
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0053_auto_20170531_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rangeattribute',
            name='values',
            field=django.contrib.postgres.fields.ranges.FloatRangeField(blank=True, default=[0, 0], verbose_name='диапазон значений'),
        ),
    ]
