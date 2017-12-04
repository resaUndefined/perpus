from django.conf.urls import url, include
from userApp import views
#from django.contrib.auth import views as auth_views


urlpatterns = [
   	url(r'^$', views.Anggota),
   	#url(r'^anggota/(?P<id>[0-9]+)/$', views.LoginView),
   	url(r'^login/$', views.LoginView),
    #url(r'^buku/$', views.buku),
    #url(r'^buku/add/$', views.tambah_buku),
    #url(r'^buku/edit/(?P<id_buku>[0-9]+)$', views.edit_buku),
    #url(r'^buku/delete/(?P<id_buku>[0-9]+)$', views.delete_buku),
]