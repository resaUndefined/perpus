# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from perpusApp.models import Katalog,Buku

# Create your views here.
def Index(request):
	katalog = Katalog.objects.all().order_by('-thn_terbit')[:5]

	data = {
		'katalog' : katalog,
	}

	return render(request, 'index.html',data)

def katalogView(request,slug):
	ktlg = Katalog.objects.get(slug=slug)
	bk = Buku.objects.filter(katalog=ktlg)
	data = {
		'ktlg' : ktlg,
		'bk'   : bk, 
	}
	return render(request,'katalog.html',data)
