from django import forms
from .models import Laboratorio 

class LaboratorioForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LaboratorioForm, self).__init__(*args, **kwargs)
        self.fields['ciudad'].widget.attrs['placeholder'] = 'Ingrese ciudad'
        self.fields['ciudad'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Laboratorio
        exclude = []