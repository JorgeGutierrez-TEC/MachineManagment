from django.db import models
from empresa.models import Empresas

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

class TipoMantenimiento(models.Model):
    id_tipo_mantenimiento = models.AutoField(primary_key=True)
    nombre_tipo_mantenimiento = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    fecha_servicio = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_mantenimiento'

class DetallemaquinariaEmpresa(models.Model):
    id_detalle_maquinaria_empresa = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)
    id_maquinaria = models.ForeignKey('Maquinaria', models.DO_NOTHING, db_column='id_maquinaria', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detallemaquinaria_empresa'


class Mantenimientos(models.Model):
    id_mantenimiento = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)
    id_maquinaria = models.ForeignKey('Maquinaria', models.DO_NOTHING, db_column='id_maquinaria', blank=True, null=True)
    id_tipo_mantenimiento = models.ForeignKey('TipoMantenimiento', models.DO_NOTHING, db_column='id_tipo_mantenimiento', blank=True, null=True)
    responsable_mantenimiento = models.ForeignKey('empleados.Empleados', models.DO_NOTHING, db_column='Responsable_mantenimiento', blank=True, null=True)
    fecha_programada = models.DateField(blank=True, null=True)
    fecha_realizacion = models.DateField(blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mantenimientos'

class PiezasMantenimiento(models.Model):
    ind_pieza_mantenimiento = models.AutoField(primary_key=True)
    id_mantenimiento = models.ForeignKey('Mantenimientos', models.DO_NOTHING, db_column='id_mantenimiento', blank=True, null=True)
    id_pieza = models.ForeignKey('inventario.Piezas', models.DO_NOTHING, db_column='id_pieza', blank=True, null=True)
    cantidad_usada = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'piezas_mantenimiento'
