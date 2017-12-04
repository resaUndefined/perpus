# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin
from userApp.models import Petugas, Anggota

# Register your models here.
admin.site.register(Petugas)
admin.site.register(Anggota)
