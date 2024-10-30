from django.db import models



# Modelo generado para la tabla empleados
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
