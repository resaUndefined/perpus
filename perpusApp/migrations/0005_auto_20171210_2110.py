# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpusApp', '0004_auto_20171210_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='katalog',
            name='foto_sampul',
            field=models.ImageField(blank=True, null=True, upload_to='image_katalog/'),
        ),
    ]
