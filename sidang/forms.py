from django import forms
from .models import tabelSidang
from mahasiswa.models import tabelMhs

class formSidang(forms.ModelForm):

    nim = forms.ModelChoiceField(queryset=tabelMhs.objects.all(), widget=forms.Select(attrs={'class': 'form-control mt-2'}))

    class Meta:
        model = tabelSidang
        fields = ['s_persetujuan', 's_permohonan', 's_undangan', 'bukti_pembayaran', 'krs', 'kartu_bimbingan', 'transkrip']
        widgets = {
            's_persetujuan'     : forms.FileInput(attrs={'class': 'form-control mt-2', 'type' : 'file'}),
            's_permohonan'      : forms.FileInput(attrs={'class': 'form-control mt-2', 'type' : 'file'}),
            's_undangan'        : forms.FileInput(attrs={'class': 'form-control mt-2', 'type' : 'file'}),
            'bukti_pembayaran'  : forms.FileInput(attrs={'class': 'form-control mt-2', 'type' : 'file'}),
            'krs'               : forms.FileInput(attrs={'class': 'form-control mt-2', 'type' : 'file'}),
            'kartu_bimbingan'   : forms.FileInput(attrs={'class': 'form-control mt-2', 'type' : 'file'}),
            'transkrip'         : forms.FileInput(attrs={'class': 'form-control mt-2', 'type' : 'file'}),
        }

class formTglSidang(forms.ModelForm):
    class Meta:
        model = tabelSidang
        fields = ['tanggal']
        widgets = {
            'tanggal'           : forms.DateTimeInput(attrs={'class': 'form-control mt-2', 'type' : 'datetime-local'}),
        }

# class formWaktuSidang(forms.ModelForm) :
#     nim = forms.ModelChoiceField(queryset=tabelMhs.objects.all(), widget=forms.Select(attrs={'class': 'form-control mt-2'}))

#     class Meta:
#         model = tabelWaktuSidang
#         fields = ['waktu_sidang']
#         widgets = {
#             'waktu_sidang'     : forms.DateTimeInput(attrs={'class': 'form-control mt-2', 'type' : 'date-time'}),
#         }


