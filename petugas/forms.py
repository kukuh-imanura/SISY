from django import forms
from . models import tabelPetugas

class formPetugas(forms.ModelForm):

    class Meta:
        model = tabelPetugas
        fields = ['nidn', 'nama', 'alamat', 'tipe', 'username', 'password']
        widgets = {
            'nidn'      : forms.NumberInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Nidn', 'type' : 'number'}),
            'nama'      : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Nama'}),
            'alamat'    : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Alamat'}),
            'tipe'      : forms.RadioSelect(attrs={'class': 'mt-2'}, choices=(
                ('prodi', 'Admin Prodi'),
                ('fakultas', 'Admin Fakultas'),
            )),
            'username'  : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Username'}),
            'password'  : forms.PasswordInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Password'}),
        }


