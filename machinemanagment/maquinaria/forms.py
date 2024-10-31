from django.forms import ModelForm
from .models import Maquinaria

class MaquinariaForm(ModelForm):
    class Meta:
        model = Maquinaria
        fields = ['nombre_maquinaria', 'modelo', 'estado', 'fecha_adquisicion']