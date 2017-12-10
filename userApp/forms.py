from django.forms import ModelForm
from userApp.models import Anggota


class AnggotaForm(ModelForm):

	class Meta:
		model = Anggota
		fields = ['nis', 'nama', 'jk', 'agama','alamat','ttl' ]