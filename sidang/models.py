from django.db import models

# Create your models here.

from mahasiswa.models import tabelMhs

class tabelSidang(models.Model) :
    id_sidang           = models.AutoField(primary_key=True)
    nim                 = models.OneToOneField(tabelMhs, on_delete=models.CASCADE)
    s_persetujuan       = models.FileField(upload_to='sidang/surat_persetujuan/')
    s_permohonan        = models.FileField(upload_to='sidang/surat_permohonan/')
    s_undangan          = models.FileField(upload_to='sidang/surat_undangan/')
    bukti_pembayaran    = models.FileField(upload_to='sidang/bukti_pembayaran/')
    krs                 = models.FileField(upload_to='sidang/krs/')
    kartu_bimbingan     = models.FileField(upload_to='sidang/kartu_bimbingan/')
    transkrip           = models.FileField(upload_to='sidang/transkrip/')
    
class tabelWaktuSidang(models.Model) :
    id_waktu_sidang     = models.AutoField(primary_key=True)
    nim                 = models.OneToOneField(tabelMhs, on_delete=models.CASCADE)
    waktu_sidang        = models.DateTimeField()