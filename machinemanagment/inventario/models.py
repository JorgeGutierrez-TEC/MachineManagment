from django.db import models

class Piezas(models.Model):
    id_pieza = models.AutoField(primary_key=True)
    nombre_pieza = models.CharField(max_length=50, blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'piezas'

class InventarioPiezas(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    cantidad_stock_piezas = models.IntegerField()
    id_pieza = models.ForeignKey('Piezas', models.DO_NOTHING, db_column='id_pieza')
    fecha_entrada = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventario_piezas'

class AddPieza(models.Model):
    id_add_pieza = models.AutoField(primary_key=True)
    id_pieza = models.ForeignKey('Piezas', models.DO_NOTHING, db_column='id_pieza', blank=True, null=True)
    id_proveedor = models.ForeignKey('ProveedorPiezas', models.DO_NOTHING, db_column='id_proveedor', blank=True, null=True)
    cantidad_piezas = models.IntegerField(blank=True, null=True)
    descripcion_pieza = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'add_pieza'

class ProveedorPiezas(models.Model):
    id_proveedor_piezas = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(db_column='Nombre_empresa', max_length=100, blank=True, null=True)  
    rfc = models.CharField(db_column='RFC', max_length=40, blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    tipo_moneda_pago = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'proveedor_piezas'
