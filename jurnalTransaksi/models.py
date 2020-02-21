from django.db import models
from jurnalApp.models import Jurnal
# Create your models here.
class transaksiJurnal(models.Model):
    jurnal   = models.ForeignKey(Jurnal,on_delete=models.CASCADE)
    tanggalJurnal = models.DateField(auto_now=False,auto_now_add=False)
    uraianJurnal  = models.TextField()
    debt   = models.FloatField(blank=True,default=0.0)
    kredit = models.FloatField(blank=True,default=0.0)

    def __str__(self):
        return self.uraianJurnal
    class Meta:
        db_table = 'transaksi'
        ordering = ['id']