from django import forms
from .models import Empresas

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresas
        fields = ['nombre_empresa', 'ubicacion_empresa', 'rfc']  # Asegúrate de usar 'rfc' en lugar de 'RFC'
