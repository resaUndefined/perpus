# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin
from perpusApp.models import Kategori, Penulis, Penerbit, Rak, Katalog
from perpusApp.models import Buku, Sirkulasi

# Register your models here.
class KatalogAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('isbn','jdl_buku','jumlah','thn_terbit','penerbit',
					'penulis','kategori','rak')
	list_filter = ('thn_terbit','penerbit','penulis','kategori','rak')
	search_fields = ('isbn','jdl_buku','thn_terbit','penerbit','penulis')
	prepopulated_fields = {'slug' : ('jdl_buku',)}


class BukuAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('get_jdl_buku','kd_itemBuku','status','kondisi','rak_buku')
	list_filter = ('status','kondisi','katalog__jdl_buku','katalog__rak')
	search_fields = ('katalog__jdl_buku','kd_itemBuku')

	def get_jdl_buku(self, obj):
		return obj.katalog.jdl_buku
	get_jdl_buku.short_description = 'Katalog'
	get_jdl_buku.admin_order_field = 'katalog__jdl_buku'

	def rak_buku(search_fields, obj):
		return obj.katalog.rak
		get_rak.short_description = 'Katalog'
		get_rak.admin_order_field = 'katalog__rak'

admin.site.site_header = 'Perpustakaan Admin'
admin.site.register(Kategori)
admin.site.register(Penulis)
admin.site.register(Penerbit)
admin.site.register(Rak)
admin.site.register(Katalog, KatalogAdmin)
admin.site.register(Buku,BukuAdmin)
admin.site.register(Sirkulasi)
