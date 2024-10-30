# resolver/forms.py
from django import forms
from .models import Empresa

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre_empresa', 'ubicacion_empresa', 'RFC', 'estado']
