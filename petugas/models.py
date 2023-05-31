from django.db import models

# Create your models here.

# BUAT TABEL ADMIN
class tabelPetugas(models.Model) :
    
    TIPE_CHOICES = (
        ('prodi', 'Admin Prodi'),
        ('fakultas', 'Admin Fakultas'),
    )

    nidn        = models.CharField(max_length=12, primary_key=True)
    nama        = models.CharField(max_length=30)
    alamat      = models.CharField(max_length=50)
    tipe        = models.CharField(max_length=8, choices=TIPE_CHOICES)
    username    = models.CharField(max_length=20)
    password    = models.CharField(max_length=32)