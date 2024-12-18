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


class Areas(models.Model):
    id_areas = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areas'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BancoEm(models.Model):
    id_banco = models.AutoField(primary_key=True)
    dinero = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banco_em'


class DetallemaquinariaEmpresa(models.Model):
    id_detalle_maquinaria_empresa = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey('Empresas', models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)
    id_maquinaria = models.ForeignKey('Maquinaria', models.DO_NOTHING, db_column='id_maquinaria', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detallemaquinaria_empresa'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class EmpresaEmpresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=100)
    ubicacion_empresa = models.CharField(max_length=250)
    rfc = models.CharField(db_column='RFC', unique=True, max_length=13)  # Field name made lowercase.
    estado = models.CharField(max_length=10)
    fecha_creacion = models.DateTimeField()
    fecha_modificacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'empresa_empresa'


class Empresas(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=100, blank=True, null=True)
    ubicacion_empresa = models.CharField(max_length=100, blank=True, null=True)
    rfc = models.CharField(db_column='RFC', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresas'


class Ganancias(models.Model):
    id_ganancia = models.AutoField(primary_key=True)
    id_reparacion = models.ForeignKey('Reparaciones', models.DO_NOTHING, db_column='id_reparacion', blank=True, null=True)
    ingresos = models.FloatField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ganancias'


class HistorialMaquinas(models.Model):
    id_historial = models.AutoField(primary_key=True)
    id_maquinaria = models.ForeignKey('Maquinaria', models.DO_NOTHING, db_column='id_maquinaria', blank=True, null=True)
    tipo_evento = models.CharField(max_length=100, blank=True, null=True)
    fecha_evento = models.DateField(blank=True, null=True)
    descripcion_evento = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historial_maquinas'


class InicioSesion(models.Model):
    id_usuario = models.OneToOneField(Empleados, models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    id_areas = models.ForeignKey(Areas, models.DO_NOTHING, db_column='id_areas', blank=True, null=True)
    usuario = models.CharField(max_length=50, blank=True, null=True)
    contrasena = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inicio_sesion'


class InventarioPiezas(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    cantidad_stock_piezas = models.IntegerField()
    id_pieza = models.ForeignKey('Piezas', models.DO_NOTHING, db_column='id_pieza')
    fecha_entrada = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventario_piezas'


class Mantenimientos(models.Model):
    id_mantenimiento = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)
    id_maquinaria = models.ForeignKey('Maquinaria', models.DO_NOTHING, db_column='id_maquinaria', blank=True, null=True)
    id_tipo_mantenimiento = models.ForeignKey('TipoMantenimiento', models.DO_NOTHING, db_column='id_tipo_mantenimiento', blank=True, null=True)
    responsable_mantenimiento = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='Responsable_mantenimiento', blank=True, null=True)  # Field name made lowercase.
    fecha_programada = models.DateField(blank=True, null=True)
    fecha_realizacion = models.DateField(blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mantenimientos'


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


class Piezas(models.Model):
    id_pieza = models.AutoField(primary_key=True)
    nombre_pieza = models.CharField(max_length=50, blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'piezas'


class PiezasMantenimiento(models.Model):
    ind_pieza_mantenimiento = models.AutoField(primary_key=True)
    id_mantenimiento = models.ForeignKey(Mantenimientos, models.DO_NOTHING, db_column='id_mantenimiento', blank=True, null=True)
    id_pieza = models.ForeignKey(Piezas, models.DO_NOTHING, db_column='id_pieza', blank=True, null=True)
    cantidad_usada = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'piezas_mantenimiento'


class ProveedorPiezas(models.Model):
    id_proveedor_piezas = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(db_column='Nombre_empresa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rfc = models.CharField(db_column='RFC', max_length=40, blank=True, null=True)  # Field name made lowercase.
    fecha_registro = models.DateField(blank=True, null=True)
    tipo_moneda_pago = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'proveedor_piezas'


class Reparaciones(models.Model):
    id_reparacion = models.AutoField(primary_key=True)
    id_maquinaria = models.ForeignKey(Maquinaria, models.DO_NOTHING, db_column='id_maquinaria', blank=True, null=True)
    fecha_reparacion = models.DateField(blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    costo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reparaciones'


class StatusStatus(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_active = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'status_status'


class TipoMantenimiento(models.Model):
    id_tipo_mantenimiento = models.AutoField(primary_key=True)
    nombre_tipo_mantenimiento = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    fecha_servicio = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_mantenimiento'
