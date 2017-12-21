from django.conf.urls import url, include
from perpusApp import views

urlpatterns = [
	url(r'^buku/$', views.Index),
  url(r'^buku/(?P<slug>[\w-]+)/$', views.katalogView),
  url(r'^cara-memesan/$', views.caraMeminjamBuku),
  url(r'^aturan-peminjaman/$', views.aturanMeminjamBuku),
   	# url(r'^$', views.Anggota),
   	# url(r'^siswa/$', views.PanelView),
   	# url(r'^siswa/akses/$', views.hakAksesView),
    # url(r'^siswa/pass/$', views.hakAksesViewUbah),
   	# url(r'^siswa/ubah-password/$', views.hakAksesUbah),
    # url(r'^siswa/edit/(?P<id>[0-9]+)/$', views.editAnggota),
    # url(r'^siswa/riwayat/$', views.riwayatView),
    #url(r'^logout/$',LogoutView),
   	#url(r'^logout/$',LogoutView),
   	#url(r'^siswa/(?P<id>[0-9]+)/$', views.PanelView),
    #url(r'^buku/$', views.buku),
    #url(r'^buku/add/$', views.tambah_buku),
    #url(r'^buku/edit/(?P<id_buku>[0-9]+)$', views.edit_buku),
    #url(r'^buku/delete/(?P<id_buku>[0-9]+)$', views.delete_buku),
]