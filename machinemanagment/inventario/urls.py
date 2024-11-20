from django.urls import path
from inventario import views

app_name = "inventario"

urlpatterns = [

# Urls para el inventario
    path('lista-inventario/', views.lista_inventarios.as_view(), name='lista_inventario'),
    path('detalle-inventario/<int:pk>/', views.DetalleInventario.as_view(), name='detalle_inventario'),

# Urls para piezas
    path('lista-piezas/', views.lista_piezas.as_view(), name='lista_piezas'),
    path('detalle-pieza/<int:pk>/', views.DetallePieza.as_view(), name='detalle_pieza'),
    path('actualizar-pieza/<int:pk>/', views.ActualizarPieza.as_view(), name='actualizar_pieza'),
    path('eliminar-pieza/<int:pk>/', views.EliminarPieza.as_view(), name='eliminar_pieza'),
    path('agregar-pieza/', views.AgregarPieza.as_view(), name='agregar_pieza'),

# Urls para añadir piezas
    path('add-pieza/', views.agregar_piezas.as_view(), name='add_pieza'),
    path('detalle-add-pieza/<int:pk>/', views.DetalleAddPieza.as_view(), name='detalle_add_pieza'),
    path('actualizar-add-pieza/<int:pk>/', views.ActualizarAddPieza.as_view(), name='actualizar_add_pieza'),
    path('eliminar-add-pieza/<int:pk>/', views.EliminarAddPieza.as_view(), name='eliminar_add_pieza'),
    path('agregar-add-pieza/', views.Agregar_stock_Pieza.as_view(), name='agregar_add_pieza'),

# Urls para proveedores
    path('lista-proveedor/', views.lista_proveedor.as_view(), name='lista_proveedor'),
    path('agregar-proveedor/', views.AgregarProveedor.as_view(), name='agregar_proveedor_pieza'),  # Agregar proveedor
    path('actualizar-proveedor/<int:pk>/', views.ActualizarProveedor.as_view(), name='actualizar_proveedor_pieza'),  # Modificar proveedor
    path('detalle-proveedor/<int:pk>/', views.DetalleProveedor.as_view(), name='detalle_proveedor_pieza'),  # Ver detalles
    path('eliminar-proveedor/<int:pk>/', views.EliminarProveedor.as_view(), name='eliminar_proveedor_pieza'),  # Eliminar proveedor
]