# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-07 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20180207_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
