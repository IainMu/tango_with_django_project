# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-08 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20180207_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='slug',
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
