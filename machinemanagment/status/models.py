from django.db import models




# Modelo generado para la tabla estatus
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Estatus(models.Model):
    id_estatus = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    fecha_creacion = models.DateTimeField(db_column='Fecha_Creacion', blank=True, null=True)  # Field name made lowercase.
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    esta_activo = models.IntegerField(blank=True, null=True)
    esta_eliminado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estatus'


# Modelo generado para la tabla ganancias
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ganancias(models.Model):
    id_ganancia = models.AutoField(primary_key=True)
    id_reparacion = models.ForeignKey('Reparaciones', models.DO_NOTHING, db_column='id_reparacion', blank=True, null=True)
    ingresos = models.FloatField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ganancias'


# Modelo generado para la tabla banco_em
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BancoEm(models.Model):
    id_banco = models.AutoField(primary_key=True)
    dinero = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banco_em'


# Modelo generado para la tabla historial_maquinas
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class HistorialMaquinas(models.Model):
    id_historial = models.AutoField(primary_key=True)
    id_maquinaria = models.ForeignKey('Maquinaria', models.DO_NOTHING, db_column='id_maquinaria', blank=True, null=True)
    tipo_evento = models.CharField(max_length=100, blank=True, null=True)
    fecha_evento = models.DateField(blank=True, null=True)
    descripcion_evento = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historial_maquinas'


# Modelo generado para la tabla reparaciones
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Reparaciones(models.Model):
    id_reparacion = models.AutoField(primary_key=True)
    id_maquinaria = models.ForeignKey('Maquinaria', models.DO_NOTHING, db_column='id_maquinaria', blank=True, null=True)
    fecha_reparacion = models.DateField(blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    costo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reparaciones'
