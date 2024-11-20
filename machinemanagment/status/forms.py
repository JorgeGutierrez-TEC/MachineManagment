from django.forms import ModelForm
from .models import Status, BancoEm, Reparaciones, HistorialMaquinas

class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['name', 'description', 'is_active']

class BancoForm(ModelForm):
    class Meta:
        model = BancoEm
        fields = ['dinero']

class ReparacionesForm(ModelForm):
    class Meta:
        model = Reparaciones
        fields =['id_maquinaria', 'fecha_reparacion', 'descripcion', 'costo']
class HistorialMaquinasform(ModelForm):
    class Meta:
        model = HistorialMaquinas
        fields = ['id_maquinaria', 'tipo_evento', 'fecha_evento', 'descripcion_evento']
