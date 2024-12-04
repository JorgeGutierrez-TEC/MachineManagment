from django.urls import path, include
from .views import CreateStatus, ListStatus, DetailStatus, UpdateStatus, DeleteStatus, graficas_view, BancoView, BancoListView, BancoDetailView, BancoUpdateView, BancoDeleteView, ReparacionesView, ReparacionesListView, ReparacionesDetailView, ReparacionesUpdateView, ReparacionesDeleteView, HistorialMaquinasView, HistorialMaquinasListView, HistorialMaquinasDetailView, HistorialMaquinasUpdateView, HistorialMaquinasDeleteView


app_name = 'status'




urlpatterns = [
    
    path('status/create/', CreateStatus.as_view(), name='status_create'),
    path('status/', ListStatus.as_view(), name='status_list'),
    path('status/graficas/', graficas_view, name='status_graficas'),  # Nueva ruta para las gráficas
    path('status/<int:pk>/', DetailStatus.as_view(), name='status_detail'),
    path('status/update/<int:pk>/', UpdateStatus.as_view(), name='status_update'),
    path('status/delete/<int:pk>/', DeleteStatus.as_view(), name='status_delete'),

    path('', BancoView.as_view(), name='banco'),
    path('list/', BancoListView.as_view(), name='bancoem_list'),
    path('<int:pk>/detalles/', BancoDetailView.as_view(), name='ver_banco'),
    path('<int:pk>/editar/', BancoUpdateView.as_view(), name='actualizar_banco'),
    path('<int:pk>/eliminar/', BancoDeleteView.as_view(), name='eliminar_banco'),

    path('reparaciones/create/', ReparacionesView.as_view(), name='reparaciones'),
    path('reparaciones/lista/', ReparacionesListView.as_view(), name='reparaciones_list'),
    path('reparaciones/detalles/<int:pk>/', ReparacionesDetailView.as_view(), name='ver_reparaciones'),
    path('reparaciones/editar/<int:pk>/', ReparacionesUpdateView.as_view(), name='actualizar_reparaciones'),
    path('reparaciones/eliminar<int:pk>/', ReparacionesDeleteView.as_view(), name='eliminar_reparaciones'),

    path('HistorialMaquinas/create/', HistorialMaquinasView.as_view(), name='historial_maquinas'),
    path('HistorialMaquinas/lista/', HistorialMaquinasListView.as_view(), name='historial_maquinas_list'),
    path('HistorialMaquinas/detalles/<int:pk>/', HistorialMaquinasDetailView.as_view(), name='ver_historial'),
    path('HistorialMaquinas/editar/<int:pk>/', HistorialMaquinasUpdateView.as_view(), name='actualizar_historial'),
    path('HistorialMaquinas/eliminar<int:pk>/', HistorialMaquinasDeleteView.as_view(), name='eliminar_historial'),
]
