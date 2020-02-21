from django import forms
from .models import Jurnal

class JurnalForm(forms.ModelForm):
    class Meta:
        model = Jurnal
        fields = ('nama','keterangan')