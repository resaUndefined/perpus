# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin
from userApp.models import Petugas, Anggota
from django.contrib.auth.models import User

# Register your models here.
class AnggotaAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('nis','nama','jk','agama','ttl','alamat','get_email',
		'get_username')
	list_filter = ('jk','agama')
	search_fields = ('nis','nama','ttl','get_username')

	def get_username(self, obj):
		return obj.user.username
	get_username.short_description = 'User'
	get_username.admin_order_field = 'user__username'

	def get_email(self, obj):
		return obj.user.email
	get_email.short_description = 'User'
	get_email.admin_order_field = 'user__email'

	# def get_status_siswa(self, obj):
	# 	return obj.user.is_active
	# get_status.short_description = 'User'
	# get_status.admin_order_field = 'user__is_active'

admin.site.register(Petugas)
admin.site.register(Anggota,AnggotaAdmin)
