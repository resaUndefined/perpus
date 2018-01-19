# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from perpusApp.models import Kategori, Penulis, Penerbit, Rak, Katalog
from perpusApp.models import Buku, Sirkulasi
from userApp.models import Anggota
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
# from import_export import resources
# from import_export.admin import ImportExportActionModelAdmin

# Register your models here.
class KatalogAdmin(admin.ModelAdmin):
	list_per_page = 15
	list_display = ('isbn','jdl_buku','jumlah','thn_terbit','penerbit',
					'penulis','kategori','rak')
	list_filter = ('thn_terbit','penerbit','penulis','kategori','rak')
	search_fields = ('isbn','jdl_buku','thn_terbit','penerbit','penulis')
	fields = ('isbn', 'kd_buku','jdl_buku','jumlah','thn_terbit',
				'foto_sampul','penerbit','penulis','kategori','rak')
	exclude = ('slug',)
	# prepopulated_fields = {'slug' : ('jdl_buku',)}


class BukuAdmin(admin.ModelAdmin):
	list_per_page = 15
	list_display = ('kd_itemBuku','get_jdl_buku','status','kondisi')
	ordering = ('kd_itemBuku',)
	list_filter = ('status','kondisi','katalog__jdl_buku','katalog__rak',)
	search_fields = ('katalog__jdl_buku','kd_itemBuku')

	def get_jdl_buku(self, obj):
		return obj.katalog.jdl_buku
	get_jdl_buku.short_description = 'Katalog'
	get_jdl_buku.admin_order_field = 'katalog__jdl_buku'

	def rak_buku(search_fields, obj):
		return obj.katalog.rak
		get_rak.short_description = 'Katalog'
		get_rak.admin_order_field = 'katalog__rak'

class SirkulasiAdmin(admin.ModelAdmin):
	list_per_page = 15
	list_display = ('kd_sirkulasi','nama_anggota','kode_Buku',
		'tgl_pinjam','tgl_kembali','jumlah_pinjam','denda','status')
	ordering = ('status',)
	list_filter = ('status',('tgl_pinjam', DateRangeFilter), 
					('tgl_kembali', DateTimeRangeFilter),)
	search_fields = ('status','kd_sirkulasi','buku__kd_itemBuku')
	fields = ('anggota', 'petugas','buku','tgl_pinjam','tgl_kembali',
				'jumlah_pinjam',)
	exclude = ('kd_sirkulasi','tgl_pesan','lama_pinjam','denda','status')
	
	def nama_anggota(self,obj):
		return obj.anggota.nama
		get_nama_anggota.short_description = "Anggota"
		get_nama_anggota.admin_order_field = 'anggota__nama'

	def kd_bk(self,obj):
		return obj.buku.kd_itemBuku
		get_kd_bk.short_description = "Buku"
		get_kd_bk.admin_order_field = 'buku__kd_itemBuku'

	def kode_Buku(self, obj):
		return "\n".join([b.kd_itemBuku + "," for b in obj.buku.all()])

	# def SirkulasiPrintOut(ImportExportActionModelAdmin):
	# 	pass

# class SirkulasiResource(resources.ModelResource):

#     class Meta:
#         model = Sirkulasi
#         fields = ('anggota', 'petugas','buku','tgl_pinjam','tgl_kembali',
# 				'jumlah_pinjam',)


# class SirkulasiPrintOut(ImportExportActionModelAdmin):
# 	pass



admin.site.site_header = 'Perpustakaan Admin'
admin.site.register(Kategori)
admin.site.register(Penulis)
admin.site.register(Penerbit)
admin.site.register(Rak)
admin.site.register(Katalog, KatalogAdmin)
admin.site.register(Buku,BukuAdmin)
admin.site.register(Sirkulasi,SirkulasiAdmin)
