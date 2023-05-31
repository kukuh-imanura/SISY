from django.db import models

# Create your models here.

from mahasiswa.models import tabelMhs

class tabelSidang(models.Model) :
    id_sidang           = models.AutoField(primary_key=True)
    nim                 = models.ForeignKey(tabelMhs, on_delete=models.CASCADE, unique=True)
    s_persetujuan       = models.FileField(upload_to='sidang/surat_persetujuan/')
    s_permohonan        = models.FileField(upload_to='sidang/surat_permohonan/')
    s_undangan          = models.FileField(upload_to='sidang/surat_undangan/')
    bukti_pembayaran    = models.FileField(upload_to='sidang/bukti_pembayaran/')
    krs                 = models.FileField(upload_to='sidang/krs/')
    kartu_bimbingan     = models.FileField(upload_to='sidang/kartu_bimbingan/')
    transkrip           = models.FileField(upload_to='sidang/transkrip/')
    