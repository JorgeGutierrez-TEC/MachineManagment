from django.db import models
from django.core.validators import RegexValidator

class Empresa(models.Model):
    ESTADOS = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]
    
    id_empresa = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=100, blank=False)
    ubicacion_empresa = models.CharField(max_length=250, blank=False)
    RFC = models.CharField(
        max_length=13, 
        unique=True,
        validators=[RegexValidator(regex='^.{13}$', message='El RFC debe tener 13 caracteres.')]
    )
    estado = models.CharField(max_length=10, choices=ESTADOS, default='activo')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_empresa

