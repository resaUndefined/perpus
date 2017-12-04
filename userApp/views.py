# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
#from userApp.forms import BukuForm
from userApp.models import Anggota
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse
from django.template import RequestContext
import datetime
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from 

# Create your views here.
def Anggota(request):
	return render(request, 'anggota/login.html')

def LoginView(request):
	if request.POST:
		#angg = User.objects.get(id=id)
		#data = {
		#		angg : 'angg',
		#	}
		username = request.POST.get('uname')
		password = request.POST.get('pass')
		is_auth = authenticate(username=username,password=password)
		if is_auth is not None:
			login(request,is_auth)
			return redirect('anggota/form.html')
		else:
			print ("gagal login, silakan cek username dan password anda")
	return render(request,'anggota/login.html')