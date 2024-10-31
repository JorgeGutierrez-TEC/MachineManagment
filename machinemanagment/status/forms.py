from django import forms
from .models import Estatus as Status

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['nombre', 'descripcion', 'esta_activo', 'esta_eliminado']
