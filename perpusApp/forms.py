from django import forms
from perpusApp.models import Sirkulasi
from django.contrib.auth.forms import UserCreationForm

class tambahSirkulasi(forms.Form):
	kd_sirkulasi = forms.CharField()
	anggota = forms.IntegerField()
	buku = forms.CharField()
	tgl_pesan = forms.CharField()

	# def save(self, commit=True):
	# 	sirkulasi = super(tambahSirkulasi, self).save(commit=False)
	# 	sirkulasi.kd_sirkulasi = self.cleaned_data['kd_sirkulasi']
	# 	sirkulasi.anggota = self.cleaned_data['id_anggota']
	# 	sirkulasi.buku = self.cleaned_data['kd_itemBuku']
	# 	sirkulasi.tgl_pesan = self.cleaned_data['tgl_pesan']

	# 	if commit:
	# 		sirkulasi.save()

	# 	return sirkulasi
# class RegistrationForm(UserCreationForm):
# 	kd_sirkulasi = forms.CharField(widget=forms.TextInput(attrs={
# 			'required':True,'class': 'form-control','value' : 
# 		}
# 		))
# 	id_anggota = forms.CharField(widget=forms.TextInput(attrs={
# 			'required':False,'class': 'form-control',
# 		}
# 		))
# 	kd_itemBuuku = forms.EmailField(widget=forms.TextInput(attrs={
# 		'required':True,'class':'form-control',
# 		}
# 		),help_text='Required. Inform a valid email address.'
# 	)
# 	username = forms.CharField(widget=forms.TextInput(attrs={
# 			'required':True,'class': 'form-control',
# 		}
# 		),help_text='Required. 150 characters or fewer. Letters, '
# 	'digits and @/./+/-/_ only.'
# 	)
# 	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
# 			'required':True,'class': 'form-control',
			 
# 		}
# 		),label='password',
# 	)
# 	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
# 			'required':True,'class': 'form-control',

# 		}
# 		),label='password confirmation',
# 		help_text='Enter the same password as before, for verification.'
# 	)
# 	#ttl = forms.DateField(required=False)

# 	class Meta:
# 		model = User
# 		fields = (
# 			'username',
# 			'first_name',
# 			'last_name',
# 			'email',
# 			'password1',
# 			'password2',
# 		)

# 	def save(self, commit=True):
# 		user = super(RegistrationForm, self).save(commit=False)
# 		user.first_name = self.cleaned_data['first_name']
# 		user.last_name = self.cleaned_data['last_name']
# 		user.email = self.cleaned_data['email']
# 		#user.ttl = self.cleaned_data['ttl']

# 		if commit:
# 			user.save()

# 		return user