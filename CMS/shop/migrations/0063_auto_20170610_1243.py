# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-10 07:43
from __future__ import unicode_literals

import django.contrib.postgres.fields.ranges
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0062_auto_20170610_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rangeattribute',
            name='values',
            field=django.contrib.postgres.fields.ranges.FloatRangeField(blank=True, null=True, verbose_name='диапазон значений'),
        ),
    ]
