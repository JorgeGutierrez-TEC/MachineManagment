import os
import django
from django.core.management import call_command
from django.db import connections

# Configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "machinemanagment.settings")
django.setup()

# Diccionario con tablas y aplicaciones
tablas = {
    'mantenimientos': 'maquinaria',
    'tipo_mantenimiento': 'maquinaria',
    'DetalleMaquinaria_empresa': 'maquinaria',
    'piezas_mantenimiento': 'maquinaria',
    'piezas': 'maquinaria',
    'maquinaria': 'maquinaria',
    'empleados': 'empleados',
    'empresas': 'empresa',
    'inventario_piezas': 'inventario',
    'add_pieza': 'inventario',
    'proveedor_piezas': 'inventario',
    'estatus': 'status',
    'ganancias': 'status',
    'banco_em': 'status',
    'historial_maquinas': 'status',
    'reparaciones': 'status',
    'Areas': 'administrador',
    'inicio_sesion': 'administrador', 
}

# Función para extraer relaciones de llaves foráneas de la base de datos
def obtener_relaciones():
    relaciones = {}
    cursor = connections['default'].cursor()
    for tabla in tablas.keys():
        cursor.execute(f"""
            SELECT COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
            FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
            WHERE TABLE_NAME = '{tabla}' AND REFERENCED_TABLE_NAME IS NOT NULL;
        """)
        relaciones[tabla] = cursor.fetchall()
    return relaciones

# Relaciones de llaves foráneas
relaciones = obtener_relaciones()

# Generar los modelos en la app correspondiente con las relaciones adecuadas
for tabla, app in tablas.items():
    with open(f"{app}/models.py", "a") as archivo:
        archivo.write(f"\n\n# Modelo generado para la tabla {tabla}\n")
        call_command("inspectdb", tabla, stdout=archivo)

        # Escribir las relaciones de llaves foráneas en los modelos
        if relaciones[tabla]:
            archivo.write("\n# Relaciones de llaves foráneas\n")
            for column, ref_table, ref_column in relaciones[tabla]:
                archivo.write(
                    f"{column} = models.ForeignKey('{ref_table}', on_delete=models.CASCADE, "
                    f"db_column='{column}', to_field='{ref_column}')\n"
                )

print("Modelos generados exitosamente para las tablas especificadas, incluyendo relaciones de llaves foráneas.")
