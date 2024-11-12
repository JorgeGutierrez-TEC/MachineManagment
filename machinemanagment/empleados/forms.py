from django.forms import ModelForm
from .models import Empleados


class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleados
        fields = ['nombre_empleado', 'apellidopaterno_empleado', 'apellidomaterno_empleado', 'telefono','correo']