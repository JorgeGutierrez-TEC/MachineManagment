from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Piezas, InventarioPiezas, ProveedorPiezas, AddPieza
from django.views import generic
from django.urls import reverse_lazy

#clases para el inventario
# Vista para la lista de inventario de piezas
class lista_inventarios(generic.ListView):
    model = InventarioPiezas
    template_name = "inventario/inventario/lista_inventario.html"
    context_object_name = "Inventario"
# Vista para el detalle del inventario
class DetalleInventario(generic.DetailView):
    model = InventarioPiezas
    template_name = "inventario/inventario/inventario_detalle.html"
    context_object_name = "inventario"
# Fin de clases para invnetario


#Clases para piezas
# Vista para la lista de piezas
class lista_piezas(generic.ListView):
    model = Piezas
    template_name = "inventario/Piezas/lista_piezas.html"
    context_object_name = "piezas"
# Vista para ver los detalles de una pieza
class DetallePieza(generic.DetailView):
    model = Piezas
    template_name = "inventario/Piezas/detalle_pieza.html"  # Asegúrate de tener este template
    context_object_name = "pieza"
# Vista para actualizar una pieza existente
class ActualizarPieza(generic.UpdateView):
    model = Piezas
    template_name = "inventario/Piezas/actualizar_pieza.html"  # Asegúrate de tener este template
    fields = ['nombre_pieza', 'precio', 'descripcion']
    success_url = reverse_lazy('inventario:lista_piezas')
# Vista para eliminar una pieza
class EliminarPieza(generic.DeleteView):
    model = Piezas
    template_name = "inventario/Piezas/eliminar_pieza.html"  # Asegúrate de tener este template
    context_object_name = "piezas"
    success_url = reverse_lazy('inventario:lista_piezas')
# Vista para agregar una nueva pieza
class AgregarPieza(generic.CreateView):
    model = Piezas
    template_name = "inventario/Piezas/agregar_pieza.html"  # Asegúrate de tener este template
    fields = ['nombre_pieza', 'precio', 'descripcion']
    success_url = reverse_lazy('inventario:lista_piezas')
#Fin de clases para Piezas


##Clases para añadir piezas
# Vista para lista añadir pieza
class agregar_piezas(generic.ListView):
    model = AddPieza
    template_name = "inventario/Add_P/lista_add_pieza.html"
    context_object_name = "add_piezas"
#Detalle de las piezas agregadas
class DetalleAddPieza(generic.DetailView):
    model = AddPieza
    template_name = 'inventario/Add_P/detalle_add_pieza.html'
    context_object_name = 'add_pieza'
#Eliminar pieza agregada
class EliminarAddPieza(generic.DeleteView):
    model = AddPieza
    template_name = 'inventario/Add_P/eliminar_add_pieza.html'
    context_object_name = 'add_pieza'
    success_url = reverse_lazy('inventario:add_pieza')
#Actualizar pieza agregada
class ActualizarAddPieza(generic.UpdateView):
    model = AddPieza
    template_name = "inventario/Add_P/actualizar_add_pieza.html"  # Asegúrate de tener este template
    fields = ['id_pieza', 'id_proveedor', 'cantidad_piezas', 'descripcion_pieza']  # Los campos que deseas permitir que se actualicen
    success_url = reverse_lazy('inventario:add_pieza')
#Agregar stock de piezas
class Agregar_stock_Pieza(generic.CreateView):
    model = AddPieza
    template_name = "inventario/Add_P/agregar_add_pieza.html"
    fields = ['id_pieza', 'id_proveedor', 'cantidad_piezas', 'descripcion_pieza']
    success_url = reverse_lazy('inventario:add_pieza')  # Redirige a la lista después de agregar
#Fin de clases para añadir piezas




#Clases para proveedores
# Vista para la lista de proveedores
class lista_proveedor(generic.ListView):
    model = ProveedorPiezas
    template_name = "inventario/Proveedor/lista_proveedor.html"
    context_object_name = "proveedores"
# Vista para agregar un nuevo proveedor
class AgregarProveedor(generic.CreateView):
    model = ProveedorPiezas
    template_name = "inventario/Proveedor/agregar_proveedor.html"
    fields = ['nombre_empresa', 'rfc', 'fecha_registro', 'tipo_moneda_pago']
    success_url = reverse_lazy('inventario:lista_proveedor')  # Redirigir a la lista de proveedores después de agregar
# Vista para actualizar un proveedor
class ActualizarProveedor(generic.UpdateView):
    model = ProveedorPiezas
    template_name = "inventario/Proveedor/actualizar_proveedor.html"
    fields = ['nombre_empresa', 'rfc', 'fecha_registro', 'tipo_moneda_pago']
    success_url = reverse_lazy('inventario:lista_proveedor')  # Redirigir a la lista de proveedores después de la actualización
# Vista para ver los detalles de un proveedor
class DetalleProveedor(generic.DetailView):
    model = ProveedorPiezas
    template_name = "inventario/Proveedor/detalle_proveedor.html"
    context_object_name = "proveedor"  # Este es el nombre con el que accederás al proveedor en el template
# Vista para eliminar un proveedor
class EliminarProveedor(generic.DeleteView):
    model = ProveedorPiezas
    template_name = "inventario/Proveedor/eliminar_proveedor.html"
    context_object_name = "proveedor"  # Este es el nombre con el que accederás al proveedor en el template
    success_url = reverse_lazy('inventario:lista_proveedor')  # Redirigir a la lista de proveedores después de eliminar
#Fin de clases para proveedores