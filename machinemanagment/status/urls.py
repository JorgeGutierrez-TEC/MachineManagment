from django.urls import path
from .views import CreateStatus, ListStatus, DetailStatus, UpdateStatus, DeleteStatus, graficas_view, BancoView, BancoListView, BancoDetailView, BancoUpdateView, BancoDeleteView



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

    
]
