from django.db import models



# Modelo generado para la tabla Areas
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Areas(models.Model):
    id_areas = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Areas'


# Modelo generado para la tabla inicio_sesion
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class InicioSesion(models.Model):
    id_usuario = models.OneToOneField('Empleados', models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    id_areas = models.ForeignKey('Areas', models.DO_NOTHING, db_column='id_areas', blank=True, null=True)
    usuario = models.CharField(max_length=50, blank=True, null=True)
    contrasena = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inicio_sesion'
