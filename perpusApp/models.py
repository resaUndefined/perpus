# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from decimal import Decimal
from userApp.models import Anggota, Petugas
# Create your models here.

# kategori : kd_kategori,nama_kat
# penulis : nama_penulis, id_penulis
# penerbit : nama_penerbit, id_penerbit
# buku : status, kondisi,kd_buku
# katalog : isbn, jumlah,jdl_buku,thn_terbit,foto_sampul,
# rak : nama_rak, id_rak

YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r, r))

STATUS_CHOICES = (
	('tersedia','Tersedia'),
	('dipinjam','Dipinjam'),
	)

STATUS_PINJAM_CHOICES = (
	('pesan','Dipesan'),
	('pinjam','Dipinjam'),
	('kembali','Kembali'),
	('telat','Telat'),
	)

KONDISI_CHOICES = (
	('baik','Baik'),
	('rusak','Rusak'),
	('hilang','Hilang')
	)

class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Kategori'

    def __unicode__(self):
        return self.nama_kategori


class Penulis(models.Model):
    nama_penulis = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Penulis'

    def __unicode__(self):
        return self.nama_penulis


class Penerbit(models.Model):
    nama_penerbit = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Penerbit'

    def __unicode__(self):
        return self.nama_penerbit


class Rak(models.Model):
    nama_rak = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Rak"

    def __unicode__(self):
        return self.nama_rak


# katalog : isbn, jumlah,jdl_buku,thn_terbit,foto_sampul,
class Katalog(models.Model):
    isbn = models.CharField(max_length=15, unique=True)
    jdl_buku = models.CharField(max_length=200,null=True,blank=True)
    jumlah = models.IntegerField(null=True,blank=True)
    slug = models.CharField(max_length=200, null=True,blank=True)
    thn_terbit = models.CharField(max_length=4,null=True)
    foto_sampul = models.ImageField(upload_to='statis/image_katalog',
                                    blank=True, null=True)
    penerbit = models.ForeignKey(Penerbit, related_name='penerbit_katalog',
                                 null=True)
    penulis = models.ForeignKey(Penulis, related_name='penulis_katalog',
                                null=True)
    kategori = models.ForeignKey(Kategori, related_name='kategori_katalog',
                                 null=True)
    rak = models.ForeignKey(Rak, related_name='rak_katalog', null=True)

    class Meta:
        verbose_name_plural = "Katalog"

    def __unicode__(self):
        return self.jdl_buku


# buku : status, kondisi,kd_buku
class Buku(models.Model):
	kd_buku = models.CharField(max_length=10,unique=True)
	status = models.CharField('Status Buku',max_length=15,
			choices=STATUS_CHOICES, default='tersedia',blank=True)
	kondisi = models.CharField('Kondisi Buku',max_length=15,
			choices=KONDISI_CHOICES,default='baik',blank=True)
	katalog = models.ForeignKey(Katalog,related_name='buku_katalog', null=True)

	class Meta:
		verbose_name_plural = "Buku"

	def __unicode__(self):
		return self.kd_buku

# sirkulasi : kd_sirkulasi, tgl_kembali, lama_pinjam, jml_pinjam
	# denda, status, tgl_pesan, tgl_pinjam
# detail_sirkulasi : id_detail_sirkulasi, (kd_buku,kd_sirkulasi)
class Sirkulasi(models.Model):
	kd_sirkulasi = models.CharField(max_length=10,unique=True)
	anggota = models.ForeignKey(Anggota, related_name='anggota_sirkulasi',
		null=True)
	tgl_pesan = models.DateField(null=True,blank=True)
	petugas = models.ForeignKey(Petugas, related_name='petugas_sirkulasi',
		null=True)
	buku = models.ManyToManyField(Buku)
	tgl_pinjam = models.DateField(null=True,blank=True)
	tgl_kembali = models.DateField(null=True,blank=True)
	lama_pinjam = models.IntegerField(null=True,blank=True)
	jumlah_pinjam = models.IntegerField(null=True)
	denda = models.DecimalField(max_digits=20,decimal_places=2,
		default=Decimal('0.00'),null=True,blank=True)
	status = models.CharField('Status Sirkulasi',max_length=20, null=True,
		choices=STATUS_PINJAM_CHOICES,blank=True)

	class Meta:
		verbose_name_plural = "Sirkulasi"

	def __unicode__(self):
		return self.kd_sirkulasi


#class Detail_Sirkulasi(models.Model):
#	sirkulasi = models.ForeignKey(Sirkulasi,
#			related_name='sirkulasi_detail', null=True)
#	buku = models.ForeignKey(Buku, related_name='detail_buku',null=True)
#
#	class Meta:
#			verbose_name_plural = "Detail_Sirkulasi"
#
#	def __unicode__(self):
#			return self.sirkulasi




