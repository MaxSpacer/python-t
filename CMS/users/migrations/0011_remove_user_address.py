# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-26 11:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20170426_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
    ]
