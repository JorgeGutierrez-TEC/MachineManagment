from django.forms import ModelForm
from .models import Maquinaria, Mantenimientos, TipoMantenimiento, PiezasMantenimiento


class MaquinariaForm(ModelForm):
    class Meta:
        model = Maquinaria
        fields = ['nombre_maquinaria', 'modelo', 'estado', 'fecha_adquisicion']

class MantenimientoForm(ModelForm):
    class Meta:
        model = Mantenimientos
        fields = ('id_empresa', 'id_maquinaria', 'id_tipo_mantenimiento', 'responsable_mantenimiento', 'fecha_programada', 'fecha_realizacion', 'descripcion')

class TipoMantenimientoForm(ModelForm):
    class Meta:
        model = TipoMantenimiento
        fields = ('nombre_tipo_mantenimiento', 'descripcion', 'precio', 'fecha_servicio')
    
class PiezasMantenimientoForm(ModelForm):
    class Meta:
        model = PiezasMantenimiento
        fields = ['id_mantenimiento', 'id_pieza', 'cantidad_usada']