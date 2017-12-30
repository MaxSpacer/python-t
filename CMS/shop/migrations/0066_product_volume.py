# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-11 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0065_auto_20170611_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='volume',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True, verbose_name='объём с упаковкой, м3'),
        ),
    ]
