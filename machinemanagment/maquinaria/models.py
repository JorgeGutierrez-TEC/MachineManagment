from django.db import models



# Modelo generado para la tabla mantenimientos
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Mantenimientos(models.Model):
    id_mantenimiento = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey('Empresas', models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)
    id_maquinaria = models.ForeignKey('Maquinaria', models.DO_NOTHING, db_column='id_maquinaria', blank=True, null=True)
    id_tipo_mantenimiento = models.ForeignKey('TipoMantenimiento', models.DO_NOTHING, db_column='id_tipo_mantenimiento', blank=True, null=True)
    responsable_mantenimiento = models.ForeignKey('Empleados', models.DO_NOTHING, db_column='Responsable_mantenimiento', blank=True, null=True)  # Field name made lowercase.
    fecha_programada = models.DateField(blank=True, null=True)
    fecha_realizacion = models.DateField(blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mantenimientos'


# Modelo generado para la tabla tipo_mantenimiento
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TipoMantenimiento(models.Model):
    id_tipo_mantenimiento = models.AutoField(primary_key=True)
    nombre_tipo_mantenimiento = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    fecha_servicio = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_mantenimiento'


# Modelo generado para la tabla DetalleMaquinaria_empresa
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DetallemaquinariaEmpresa(models.Model):
    id_detalle_maquinaria_empresa = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey('Empresas', models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)
    id_maquinaria = models.ForeignKey('Maquinaria', models.DO_NOTHING, db_column='id_maquinaria', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DetalleMaquinaria_empresa'


# Modelo generado para la tabla piezas_mantenimiento
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PiezasMantenimiento(models.Model):
    ind_pieza_mantenimiento = models.AutoField(primary_key=True)
    id_mantenimiento = models.ForeignKey('Mantenimientos', models.DO_NOTHING, db_column='id_mantenimiento', blank=True, null=True)
    id_pieza = models.ForeignKey('Piezas', models.DO_NOTHING, db_column='id_pieza', blank=True, null=True)
    cantidad_usada = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'piezas_mantenimiento'


# Modelo generado para la tabla piezas
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Piezas(models.Model):
    id_pieza = models.AutoField(primary_key=True)
    nombre_pieza = models.CharField(max_length=50, blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'piezas'


# Modelo generado para la tabla maquinaria
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Maquinaria(models.Model):
    id_maquinaria = models.AutoField(primary_key=True)
    nombre_maquinaria = models.CharField(max_length=100, blank=True, null=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    fecha_adquisicion = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maquinaria'
