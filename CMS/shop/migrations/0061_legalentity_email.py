# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-04 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0060_auto_20170604_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='legalentity',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='электронная почта'),
        ),
    ]
