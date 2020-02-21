from django.db import models

# Create your models here.
class Jurnal(models.Model):
    nama = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=255)
    