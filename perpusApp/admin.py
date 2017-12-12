# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin
from perpusApp.models import Kategori, Penulis, Penerbit, Rak, Katalog
from perpusApp.models import Buku, Sirkulasi

# Register your models here.
class KatalogAdmin(admin.ModelAdmin):
	list_display = ('isbn','jdl_buku','jumlah','thn_terbit','penerbit',
					'penulis','kategori','rak')
	list_filter = ('thn_terbit','penerbit','penulis','kategori','rak')
	search_fields = ('isbn','jdl_buku','thn_terbit','penerbit','penulis')
	prepopulated_fields = {'slug' : ('jdl_buku',)}


class BukuAdmin(admin.ModelAdmin):
	list_display = ('kd_buku','status','kondisi')
	list_filter = ('status','kondisi')
	# search_fields = ('kd_buku')

admin.site.site_header = 'Perpustakaan Admin'
admin.site.register(Kategori)
admin.site.register(Penulis)
admin.site.register(Penerbit)
admin.site.register(Rak)
admin.site.register(Katalog, KatalogAdmin)
admin.site.register(Buku,BukuAdmin)
admin.site.register(Sirkulasi)
