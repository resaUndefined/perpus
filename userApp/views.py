# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from userApp.models import Anggota
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse
from django.template import RequestContext
import datetime
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from userApp.forms import AnggotaForm
#from 

# Create your views here.
def Anggota(request):
	data = {
				'user' : request.user,
			}
	return render(request, 'anggota/login.html',data)

#@login_required(login_url='/login/')
def PanelView(request):
	data = {
				'user' : request.user,
			}
	if request.user.is_authenticated():
		
		return render(request,'anggota/form.html',data)

	if request.POST:
		data = {
				'user' : request.user,
			}
		username = request.POST.get('uname')
		password = request.POST.get('pass')
		is_auth = authenticate(username=username,password=password)
		if is_auth is not None:
			login(request,is_auth)
			return render(request,'anggota/form.html',data)
		else:
			print ("gagal login, silakan cek username dan password anda")
	return render(request,'anggota/login.html')

def LogoutView(request):
	logout(request)
	return redirect('/')

def hakAksesView(request):
	data = {
		'user' : request.user,
	}
	return render(request, 'anggota/hakAkses.html',data)

def hakAksesViewUbah(request):
	form = PasswordChangeForm(request.user)
	data = {
		'user' : request.user,
		'form' : form,
	}
	return render(request, 'anggota/hakAksesUbah.html',data)

def hakAksesUbah(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/login/siswa/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'anggota/hakAksesUbah.html', {
        'form': form
    })

def editAnggota(request, id):
	data_anggota = User.objects.get(id=id)
	if request.method == 'POST':
		form = AnggotaForm(request.POST, instance=data_anggota)
		if form.is_valid():
			form.save()
			return redirect('/login/siswa/')
	else:
		form = AnggotaForm(instance=data_anggota) 

	data = {
		'form': form,
	}
	return render(request, 'anggota/formUbah.html', data)

def riwayatView(request):

	return render(request, 'anggota/riwayat.html')
	 