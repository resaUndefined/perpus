# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 17:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anggota',
            name='email',
        ),
        migrations.RemoveField(
            model_name='anggota',
            name='pass_id',
        ),
        migrations.RemoveField(
            model_name='anggota',
            name='status',
        ),
        migrations.RemoveField(
            model_name='petugas',
            name='email',
        ),
        migrations.RemoveField(
            model_name='petugas',
            name='pass_id',
        ),
        migrations.AlterField(
            model_name='anggota',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='petugas',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]