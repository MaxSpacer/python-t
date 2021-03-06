# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-01 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0057_remove_variantfilter_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decimalfilter',
            name='unit',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='единица измерения'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rangefilter',
            name='unit',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='единица измерения'),
            preserve_default=False,
        ),
    ]
