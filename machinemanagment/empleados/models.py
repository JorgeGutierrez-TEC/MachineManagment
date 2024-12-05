from django.db import models

# Create your models here.
class Empleados(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre_empleado = models.CharField(max_length=50, blank=True, null=True)
    apellidomaterno_empleado = models.CharField(db_column='apellidoMaterno_empleado', max_length=50, blank=True, null=True)  # Field name made lowercase.
    apellidopaterno_empleado = models.CharField(db_column='apellidoPaterno_empleado', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telefono = models.FloatField(blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleados'
        