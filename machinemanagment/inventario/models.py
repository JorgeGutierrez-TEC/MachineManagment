from django.db import models

# 

# Modelo generado para la tabla inventario_piezas
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class InventarioPiezas(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    cantidad_stock_piezas = models.IntegerField()
    id_pieza = models.ForeignKey('Piezas', models.DO_NOTHING, db_column='id_pieza')
    fecha_entrada = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventario_piezas'


# Modelo generado para la tabla add_pieza
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AddPieza(models.Model):
    id_add_pieza = models.AutoField(primary_key=True)
    id_pieza = models.ForeignKey('Piezas', models.DO_NOTHING, db_column='id_pieza', blank=True, null=True)
    id_proveedor = models.ForeignKey('ProveedorPiezas', models.DO_NOTHING, db_column='id_proveedor', blank=True, null=True)
    cantidad_piezas = models.IntegerField(blank=True, null=True)
    descripcion_pieza = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'add_pieza'


# Modelo generado para la tabla proveedor_piezas
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ProveedorPiezas(models.Model):
    id_proveedor_piezas = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(db_column='Nombre_empresa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rfc = models.CharField(db_column='RFC', max_length=40, blank=True, null=True)  # Field name made lowercase.
    fecha_registro = models.DateField(blank=True, null=True)
    tipo_moneda_pago = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'proveedor_piezas'
