from django.conf.urls import url, include
from userApp import views
#from django.contrib.auth import views as auth_views


urlpatterns = [
   	url(r'^$', views.Anggota),
   	url(r'^siswa/$', views.PanelView),
   	url(r'^siswa/akses/$', views.hakAksesView),
    url(r'^siswa/pass/$', views.hakAksesViewUbah),
   	url(r'^siswa/ubah-password/$', views.hakAksesUbah),
    url(r'^siswa/edit/(?P<id>[0-9]+)/$', views.editAnggota),
    url(r'^siswa/riwayat/(?P<id>[0-9]+)/$', views.riwayatView),
    #url(r'^logout/$',LogoutView),
   	#url(r'^logout/$',LogoutView),
   	#url(r'^siswa/(?P<id>[0-9]+)/$', views.PanelView),
    #url(r'^buku/$', views.buku),
    #url(r'^buku/add/$', views.tambah_buku),
    #url(r'^buku/edit/(?P<id_buku>[0-9]+)$', views.edit_buku),
    #url(r'^buku/delete/(?P<id_buku>[0-9]+)$', views.delete_buku),
]