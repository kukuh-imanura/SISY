from django import forms
from .models import tabelYudisium

from mahasiswa.models import tabelMhs

class formYudisium(forms.ModelForm):
    nim = forms.ModelChoiceField(queryset=tabelMhs.objects.all(), widget=forms.Select(attrs={'class': 'form-control mt-2'}))
    class Meta:
        model = tabelYudisium
        fields = ['transkrip', 'sertifikat_toefl', 'sertifikat_publicSpeaking', 'sertifikat_keahlian', 'sk_bebasPembayaran', 'sk_bebasPinjaman', 'sk_bebasPlagiasi', 'bukti_pembayaran']
        widgets = {
            'transkrip'                 : forms.FileInput(attrs={'class': 'form-control mt-2', 'type' : 'file'}),
            'sertifikat_toefl'          : forms.FileInput(attrs={'class': 'form-control mt-2', 'type' : 'file'}),
            'sertifikat_publicSpeaking' : forms.FileInput(attrs={'class': 'form-control mt-2', 'type' : 'file'}),
            'sertifikat_keahlian'       : forms.FileInput(attrs={'class': 'form-control mt-2', 'type' : 'file'}),
            'sk_bebasPembayaran'        : forms.FileInput(attrs={'class': 'form-control mt-2', 'type' : 'file'}),
            'sk_bebasPinjaman'          : forms.FileInput(attrs={'class': 'form-control mt-2', 'type' : 'file'}),
            'sk_bebasPlagiasi'          : forms.FileInput(attrs={'class': 'form-control mt-2', 'type' : 'file'}),
            'bukti_pembayaran'          : forms.FileInput(attrs={'class': 'form-control mt-2', 'type' : 'file'}),
        }

class formTglYudisium(forms.ModelForm):
    nim = forms.ModelChoiceField(queryset=tabelMhs.objects.all(), widget=forms.Select(attrs={'class': 'form-control mt-2'}))
    class Meta:
        model = tabelYudisium
        fields = ['tanggal']
        widgets = {
            'tanggal'   : forms.DateTimeInput(attrs={'class': 'form-control mt-2', 'type' : 'datetime-local'}),
        }
