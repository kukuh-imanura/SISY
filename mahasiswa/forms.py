from django import forms
from . models import tabelMhs

class formMhs(forms.ModelForm):
    class Meta:
        model = tabelMhs
        fields = ['nim', 'nama', 'prodi', 'fakultas', 'username', 'password']
        widgets = {
            'nim'       : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Nim'}),
            'nama'      : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Nama'}),
            'prodi'     : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Prodi'}),
            'fakultas'  : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Fakultas'}),
            'username'  : forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Username'}),
            'password'  : forms.PasswordInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Password'}),
        }
