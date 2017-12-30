# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-24 07:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_is_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_seller',
            field=models.BooleanField(default=False, help_text='Пользователь может просматривать заказы только своих клиентов.', verbose_name='является менеджером по продажам'),
        ),
        migrations.AlterField(
            model_name='user',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer_set', to=settings.AUTH_USER_MODEL, verbose_name='менеджер покупателя'),
        ),
    ]
