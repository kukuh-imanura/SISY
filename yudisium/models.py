from django.db import models

# Create your models here.

from mahasiswa.models import tabelMhs

class tabelYudisium(models.Model) :
    id_yudisium                 = models.AutoField(primary_key=True)
    nim                         = models.OneToOneField(tabelMhs, on_delete=models.CASCADE)
    tanggal                     = models.DateTimeField()
    transkrip                   = models.FileField(upload_to='yudisium/transkrip')
    sertifikat_toefl            = models.FileField(upload_to='yudisium/toefl/')
    sertifikat_publicSpeaking   = models.FileField(upload_to='yudisium/public_speaking/')
    sertifikat_keahlian         = models.FileField(upload_to='yudisium/sertifikat_keahlian/')
    sk_bebasPembayaran          = models.FileField(upload_to='yudisium/bebas_pembayaran/')
    sk_bebasPinjaman            = models.FileField(upload_to='yudisium/bebas_pinjaman/')
    sk_bebasPlagiasi            = models.FileField(upload_to='yudisium/bebas_plagiasi/')
    bukti_pembayaran            = models.FileField(upload_to='yudisium/pembayaran/')
    