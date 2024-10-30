import os
import django
from django.core.management import call_command

# Establece la configuración de Django
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
    'banco_em': 'status',
    'reparaciones': 'status',
    'Areas': 'administrador',
    'inicio_sesion': 'administrador', 

}


# Generar los modelos en la app correcta
for tabla, app in tablas.items():
    with open(f"{app}/models.py", "a") as archivo:
        archivo.write(f"\n\n# Modelo generado para la tabla {tabla}\n")
        call_command("inspectdb", tabla, stdout=archivo)

print("Modelos generados exitosamente para las tablas especificadas.")
