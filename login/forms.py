from django import forms
from mahasiswa.models import tabelMhs

class formLogin(forms.ModelForm):
    class Meta:
        model = tabelMhs
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Masukkan Password'}),
        }