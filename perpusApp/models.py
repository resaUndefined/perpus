# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from decimal import Decimal
from userApp.models import Anggota, Petugas
from django.utils.text import slugify
from django.dispatch import receiver
# Create your models here.

YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r, r))

STATUS_CHOICES = (
    ('Tersedia', 'Tersedia'),
    ('Dipinjam', 'Dipinjam'),
)

STATUS_PINJAM_CHOICES = (
    ('Dipesan', 'Dipesan'),
    ('Dipinjam', 'Dipinjam'),
    ('Kembali', 'Kembali'),
    ('Telat', 'Telat'),
)

KONDISI_CHOICES = (
    ('Baik', 'Baik'),
    ('Rusak', 'Rusak'),
    ('Hilang', 'Hilang')
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


class Katalog(models.Model):
    isbn = models.CharField(max_length=50, unique=True)
    kd_buku = models.CharField(max_length=5, unique=True, null=True)
    jdl_buku = models.CharField(max_length=200, null=True, blank=True)
    jumlah = models.IntegerField(null=True, blank=True)
    slug = models.CharField(max_length=200, null=True, blank=True)
    thn_terbit = models.CharField(max_length=4, null=True)
    foto_sampul = models.ImageField(upload_to='image_katalog/',
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

    def save(self, *args, **kwargs):
        if self.pk is not None:
            self.slug = slugify(self.jdl_buku)
            jml = self.jumlah
            super(Katalog, self).save(*args, **kwargs)
            for i in range(self.jumlah):
                created = self.buku_katalog.get_or_create(
                    kd_itemBuku=self.kd_buku + str(i+1))
                # if created:
                # 	self.buku_katalog.create(kd_itemBuku = self.kd_buku
                # 	+ str(i+1))
                # else:
                # 	self.buku_katalog.update(kd_itemBuku = self.kd_buku
                # 	+ str(i+1))
        else:
            self.slug = slugify(self.jdl_buku)
            super(Katalog, self).save(*args, **kwargs)
            for i in range(self.jumlah):
                self.buku_katalog.create(kd_itemBuku=self.kd_buku
                                         + str(i+1))


class Buku(models.Model):
    kd_itemBuku = models.CharField(
        'Kode Buku', max_length=10, unique=True, null=True)
    status = models.CharField('Status Buku', max_length=15,
                              choices=STATUS_CHOICES, default='Tersedia',
                              blank=True)
    kondisi = models.CharField('Kondisi Buku', max_length=15,
                               choices=KONDISI_CHOICES, default='Baik',
                               blank=True)
    katalog = models.ForeignKey(
        Katalog, related_name='buku_katalog', null=True)

    class Meta:
        verbose_name_plural = "Buku"
    # list_filter = ('katalog__jdl_buku','status','kondisi',)

    def __unicode__(self):
        return self.kd_itemBuku


class Sirkulasi(models.Model):
    kd_sirkulasi = models.CharField(max_length=50, unique=True, blank=True)
    anggota = models.ForeignKey(Anggota, related_name='anggota_sirkulasi',
                                null=True)
    tgl_pesan = models.DateField(null=True, blank=True)
    petugas = models.ForeignKey(Petugas, related_name='petugas_sirkulasi',
                                null=True, blank=True)
    buku = models.ManyToManyField(Buku, related_name='buku_sirkulasi',
                                    blank=True)
    tgl_pinjam = models.DateField(null=True, blank=True)
    tgl_kembali = models.DateField(null=True, blank=True)
    lama_pinjam = models.IntegerField(null=True, blank=True)
    jumlah_pinjam = models.IntegerField(null=True, blank=True)
    denda = models.DecimalField(max_digits=20, decimal_places=2,
                                default=Decimal('0.00'), null=True, blank=True)
    status = models.CharField('Status Sirkulasi', max_length=20, null=True,
                              choices=STATUS_PINJAM_CHOICES, blank=True)

    class Meta:
        verbose_name_plural = "Sirkulasi"

    def __unicode__(self):
        return self.kd_sirkulasi

    def buku_dipinjam(self):
        bukuPinjam = self.buku.all()
        print bukuPinjam
        print self.pk
        for bp in bukuPinjam:
            bp.status = 'Tersedia'
            bp.save()

    # def banyak_pinjam(self):
    #     bukuBanyak = self.buku.all()
    #     bb = bukuBanyak.count()
    #     self.jumlah_pinjam = bb
    #     self.save()

    def save(self, *args, **kwargs):
        if self.tgl_kembali is not None:
            # self.kd_sirkulasi = datetime.datetime.now()
            pjm = self.tgl_pinjam
            pjm2 = pjm.day
            kml = self.tgl_kembali
            kml2 = kml.day
            self.status = 'Kembali'
            self.lama_pinjam = kml2 - pjm2 
            if self.lama_pinjam > 7:
                lebihnya = self.lama_pinjam - 7
                self.denda = (lebihnya * 100 * self.jumlah_pinjam)
                super(Sirkulasi, self).save(*args, **kwargs)
            else:
                lebihnya = 0
                self.denda = (lebihnya * 100 * self.jumlah_pinjam)
                super(Sirkulasi, self).save(*args, **kwargs)
                
            self.buku_dipinjam()
        else:
            d = datetime.datetime.now().time()
            jam = d.hour
            menit = d.minute
            sekon = d.second 
            self.kd_sirkulasi = str(datetime.datetime.now().day) + str(datetime.datetime.now().month) + str(datetime.datetime.now().year) + str(jam) + str(menit) + str(sekon)
            # self.banyak_pinjam()
            self.status = 'Dipinjam'
            super(Sirkulasi, self).save(*args, **kwargs)
            
            # for i in range(self.jumlah_pinjam):
            #     self.bk.get_or_create(status='Dipinjam')

@receiver(models.signals.m2m_changed, sender=Sirkulasi.buku.through)
def sirkulasi_buku_simpan(sender, instance, **kwargs):
    for b in instance.buku.all():
        b.status = 'Dipinjam'
        b.save()
# class Detail_Sirkulasi(models.Model):
#	sirkulasi = models.ForeignKey(Sirkulasi,
#			related_name='sirkulasi_detail', null=True)
#	buku = models.ForeignKey(Buku, related_name='detail_buku',null=True)
#
#	class Meta:
#			verbose_name_plural = "Detail_Sirkulasi"
#
#	def __unicode__(self):
#			return self.sirkulasi
