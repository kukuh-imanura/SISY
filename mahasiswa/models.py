from django.db import models

# Create your models here.

class tabelMhs(models.Model) :
    nim         = models.CharField(max_length=9, primary_key=True)
    nama        = models.CharField(max_length=30)
    prodi       = models.CharField(max_length=30)
    fakultas    = models.CharField(max_length=30)
    username    = models.CharField(max_length=20)
    password    = models.CharField(max_length=20)