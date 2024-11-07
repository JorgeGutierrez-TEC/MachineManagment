from django.db import models
from maquinaria.models import Maquinaria

class Status(models.Model):
    id = models.AutoField(primary_key=True)  # Clave primaria autoincremental
    name = models.CharField(max_length=50)  # Nombre del estado
    description = models.CharField(max_length=200, blank=True, null=True)  # Descripción opcional del estado
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de la última actualización
    is_active = models.BooleanField(default=True)  # Indica si el estado está activo
    is_deleted = models.BooleanField(default=False)  # Indica si el estado está eliminado

    def __str__(self):
        return self.name

class Ganancias(models.Model):
    id_ganancia = models.AutoField(primary_key=True)
    id_reparacion = models.ForeignKey('Reparaciones', models.DO_NOTHING, db_column='id_reparacion', blank=True, null=True)
    ingresos = models.FloatField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ganancias'

class BancoEm(models.Model):
    id_banco = models.AutoField(primary_key=True)
    dinero = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banco_em'

class Reparaciones(models.Model):
    id_reparacion = models.AutoField(primary_key=True)
    id_maquinaria = models.ForeignKey(Maquinaria, models.DO_NOTHING, db_column='id_maquinaria', blank=True, null=True)
    fecha_reparacion = models.DateField(blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    costo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reparaciones'

class HistorialMaquinas(models.Model):
    id_historial = models.AutoField(primary_key=True)
    id_maquinaria = models.ForeignKey(Maquinaria, models.DO_NOTHING, db_column='id_maquinaria', blank=True, null=True)
    tipo_evento = models.CharField(max_length=100, blank=True, null=True)
    fecha_evento = models.DateField(blank=True, null=True)
    descripcion_evento = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historial_maquinas'