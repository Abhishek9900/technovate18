# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-08 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='celeb',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='total',
            field=models.IntegerField(default=150),
        ),
    ]
