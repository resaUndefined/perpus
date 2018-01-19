# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from userApp.models import Anggota
from perpusApp.models import Sirkulasi
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.utils.text import slugify
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
	if request.user.is_authenticated():
		
		return render(request,'anggota/form.html',data)
	else:
		return render(request, 'anggota/login.html',data)

#@login_required(login_url='/login/')
def PanelView(request):
	data = {
				'user' : request.user,
			}
	if request.user.is_authenticated():
		
		return render(request,'anggota/form.html',data)

	if request.POST:
		username = request.POST.get('uname')
		password = request.POST.get('pass')
		is_auth = authenticate(username=username,password=password)
		if is_auth is not None:
			data = {
				'user' : request.user,
			}
			login(request,is_auth)
			return render(request,'anggota/form.html',data)
		else:
			messages.warning(
                request, 'Gagal. Silahkan cek user dan password anda')
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

def riwayatView(request,id): 
	# ang = Anggota.objects.get(user=upk)
	# anggo = Anggota.objects.get(id=id)
	sir = Sirkulasi.objects.filter(anggota=id)
	data = {
		# 'anggo' : anggo,
		'sir' : sir,
	}
	return render(request, 'anggota/riwayat.html',data)
	 