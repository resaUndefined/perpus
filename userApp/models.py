# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.

# nama, jk, alamat, email, foto, user_id, pass,
# ttl, status

JK_CHOICES = (
    ('laki', 'Laki-Laki'),
    ('perempuan', 'Perempuan'),
)

AGAMA_CHOICES = (
    ('islam', 'Islam'),
    ('kristen', 'Kristen'),
    ('katholik', 'Katholik'),
    ('hindu', 'Hindu'),
    ('budha', 'Budha'),
    ('other', 'Other'),
)
STATUS_CHOICES = (
    ('0', 'Tidak Aktif'),
    ('1', 'Aktif'),
)


class Anggota(models.Model):
    nis = models.CharField(max_length=15, unique=True)
    nama = models.CharField(max_length=100, null=True,blank=True)
    jk = models.CharField('Jenis Kelamin', max_length=15,
                           choices=JK_CHOICES, default='laki',null=True,
                           blank=True)
    agama = models.CharField('Agama', max_length=20,choices=AGAMA_CHOICES,
    						default='islam', null=True, blank=True)
    alamat = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=100)
    foto = models.ImageField(upload_to='statis/image_anggota',
                             blank=True, null=True)
    user_id = models.CharField(max_length=15)
    pass_id = models.CharField(max_length=15)
    ttl = models.DateField('Tanggal Lahir', max_length=8, null=True,blank=True)
    status = models.CharField('Status', max_length=15,choices=STATUS_CHOICES,
    						default='1',null=True, blank=True)

    class Meta:
    	verbose_name_plural = "Anggota"


    def __unicode__(self):
    	return self.nama


class Petugas(models.Model):
	kd_petugas = models.CharField(max_length=10,unique=True)
	nama = models.CharField(max_length=100, null=True, blank=True)
	user_id = models.CharField(max_length=20)
	pass_id = models.CharField(max_length=20)
	email = models.EmailField(max_length=100)
	jk = models.CharField('Jenis Kelamin',max_length=20,choices=JK_CHOICES,
						default='laki', null=True, blank=True)
	alamat = models.TextField(blank=True,null=True)
	ttl = models.DateField('tanggal Lahir',max_length=8,null=True,blank=True)
	agama = models.CharField('Agama', max_length=20, choices=AGAMA_CHOICES,
						default='islam',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Petugas"


	def __unicode__(self):
		return self.nama
