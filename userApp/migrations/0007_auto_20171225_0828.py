# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-25 01:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0006_auto_20171210_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anggota',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_anggota', to=settings.AUTH_USER_MODEL),
        ),
    ]
