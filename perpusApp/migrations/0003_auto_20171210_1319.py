# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpusApp', '0002_auto_20171121_0057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buku',
            name='kd_buku',
        ),
        migrations.AddField(
            model_name='buku',
            name='kd_itemBuku',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='katalog',
            name='kd_buku',
            field=models.CharField(max_length=5, null=True, unique=True),
        ),
    ]
