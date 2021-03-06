# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from perpusApp.models import Katalog,Buku, Kategori, Sirkulasi
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from django.contrib.auth.decorators import login_required
from perpusApp.forms import tambahSirkulasi
# Create your views here.
def Index(request):
	cate = Kategori.objects.all()
	katalog = Katalog.objects.all().order_by('-thn_terbit')[:15]
	data = {
		'cate'	  : cate,
		'katalog' : katalog,
	}
	return render(request, 'index.html',data)

def katalogView(request,slug):
	ktlg = Katalog.objects.get(slug=slug)
	cate = Kategori.objects.all()
	bk = Buku.objects.filter(katalog=ktlg)
	data = {
		'cate'	  : cate,
		'ktlg' : ktlg,
		'bk'   : bk, 
	}
	return render(request,'katalog.html',data)

def kategoriView(request,id):
	# katalog = Katalog.objects.all()
	cate2 = Kategori.objects.get(id=id)
	cate = Kategori.objects.all()
	detailCate = Katalog.objects.filter(kategori=cate2)
	data = {
		# 'katalog' : katalog,
		'cate'	  : cate,
		'detailCate' : detailCate,
		'cate2'	: cate2,
		# 'bk'   : bk, 
	}
	return render(request,'kategori.html',data)

def caraMeminjamBuku(request):
	cate = Kategori.objects.all()
	katalog = Katalog.objects.all().order_by('-thn_terbit')[:5]

	data = {
		'cate'	  : cate,
		'katalog' : katalog,
	}
	return render(request,'cara_pinjam.html',data)

def aturanMeminjamBuku(request):
	cate = Kategori.objects.all()
	katalog = Katalog.objects.all().order_by('-thn_terbit')[:5]

	data = {
		'cate'	  : cate,
		'katalog' : katalog,
	}
	return render(request,'aturan_pinjam.html',data)

def hubungiKami(request):
	cate = Kategori.objects.all()
	katalog = Katalog.objects.all().order_by('-thn_terbit')[:5]

	data = {
		'cate'	  : cate,
		'katalog' : katalog,
	}
	return render(request,'contact.html',data)

@login_required(login_url='/login/')
def BukuPesanView(request, kd_itemBuku):
	bk = Buku.objects.get(kd_itemBuku=kd_itemBuku)
	d = datetime.datetime.now().time()
	jam = d.hour
	menit = d.minute
	sekon = d.second
	day = datetime.datetime.now().day
	mon = datetime.datetime.now().month
	thn = datetime.datetime.now().year
	kd_sir = str(day) + str(mon) + str(thn) + str(jam) + str(menit) + str(sekon)
	pesan_date = datetime.date.today()
	user = request.user
	print user
	data = {
		'user' : user,
		'bk' : bk,
		'kd_sir' : kd_sir,
		'pesan_date' : pesan_date,
	}
	return render(request, 'pesan.html',data)

def BukuPesanProses(request):
	if request.method == 'POST':
		form = tambahSirkulasi(request.POST)
		if form.is_valid():

			kd_sirkulasi = request.POST.get('kd_sirkulasi','')
			anggota = request.POST.get('anggota','')
			buku = request.POST.get('buku','')
			tgl_psn = request.POST.get('tgl_pesan','')
			tgl_pesan = datetime.datetime.strptime(tgl_psn, '%b. %d, %Y')
			stat = 'Dipesan'
			print kd_sirkulasi
			print anggota
			print buku
			print tgl_pesan
			print stat
			sir_obj = Sirkulasi(kd_sirkulasi = kd_sirkulasi, anggota_id = anggota,
								 tgl_pesan = tgl_pesan, 
								status = stat)
			sir_obj.save()
			bk = Buku.objects.get(kd_itemBuku=buku)
			print bk
			sir_obj.buku.add(bk)
			bk.status = 'Dipinjam'
			bk.save()
			return HttpResponseRedirect('/')
		else:
			print request.POST
			print form.errors
			return HttpResponseRedirect('/')
	else:
		ktlg = Katalog.objects.get(slug=slug)
		cate = Kategori.objects.all()
		bk = Buku.objects.filter(katalog=ktlg)
		data = {
			'cate'	  : cate,
			'ktlg' : ktlg,
			'bk'   : bk, 
		}
		return render(request,'katalog.html', data)
