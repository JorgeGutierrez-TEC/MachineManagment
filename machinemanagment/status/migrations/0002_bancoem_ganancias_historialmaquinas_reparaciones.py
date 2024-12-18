# Generated by Django 5.1.2 on 2024-11-04 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BancoEm',
            fields=[
                ('id_banco', models.AutoField(primary_key=True, serialize=False)),
                ('dinero', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'banco_em',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ganancias',
            fields=[
                ('id_ganancia', models.AutoField(primary_key=True, serialize=False)),
                ('ingresos', models.FloatField(blank=True, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ganancias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HistorialMaquinas',
            fields=[
                ('id_historial', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_evento', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_evento', models.DateField(blank=True, null=True)),
                ('descripcion_evento', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'historial_maquinas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reparaciones',
            fields=[
                ('id_reparacion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_reparacion', models.DateField(blank=True, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('costo', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'reparaciones',
                'managed': False,
            },
        ),
    ]
