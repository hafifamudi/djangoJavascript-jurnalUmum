from django import forms
from .models import transaksiJurnal
import datetime

class TanggalJurnal(forms.DateInput):
    input_type = 'date'

class jurnalTransaksiForm(forms.Form):
    id      = forms.CharField(widget=forms.HiddenInput(),required=False)
    tanggalJurnal = forms.DateField(
        initial = datetime.date.today,widget=TanggalJurnal)
    uraianJurnal = forms.CharField(required=False,widget=forms.Textarea)
    debt = forms.FloatField(required=False,initial=0)
    kredit = forms.FloatField(required=False, initial=0)

    class Meta:
        model = transaksiJurnal