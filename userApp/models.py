# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save

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
    foto = models.ImageField(upload_to='image_anggota/',
                             blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ttl = models.DateField('Tanggal Lahir', max_length=8, null=True,blank=True)

    class Meta:
    	verbose_name_plural = "Anggota"

    def __unicode__(self):
        return self.nama

#def create_profile(sender, **kwargs):
#    if kwargs['created']:
  #      anggota = Anggota.objects.create(user=kwargs['instance'])

#post_save.connect(create_profile, sender=User)


class Petugas(models.Model):
	kd_petugas = models.CharField(max_length=10,unique=True)
	nama = models.CharField(max_length=100, null=True, blank=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
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
