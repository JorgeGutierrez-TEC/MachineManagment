from django.urls import path

from inventario import views

app_name = "inventario"

urlpatterns = [

    path('piezas/lista/', views.Piezas.as_view(), name='lista_piezas'),
    path('lista/', views.InventarioPiezas.as_view(), name='lista_inventario'),
    path('proveedor/lista/', views.Proveedores.as_view(), name='lista_proveedor'),
]