# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-22 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpusApp', '0011_auto_20171222_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sirkulasi',
            name='kd_sirkulasi',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]
