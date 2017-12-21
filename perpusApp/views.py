# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from perpusApp.models import Katalog,Buku, Kategori
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def Index(request):
	cate = Kategori.objects.all()
	katalog = Katalog.objects.all()#.order_by('-thn_terbit')[:5]
	page = request.GET.get('page', 1)
	paginator = Paginator(katalog, 4)

	try:
		kata = paginator.page(page)
	except PageNotAnInteger:
		kata = paginator.page(1)
	except EmptyPage:
		kata = paginator.page(paginator.num_pages)

	data = {
		'cate'	  : cate,
		'katalog' : katalog,
		'kata'	  : kata,
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
