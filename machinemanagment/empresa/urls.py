# resolver/urls.py
from django.urls import path
from . import views
from .views import lista_empresas, crear_empresa, actualizar_empresa, eliminar_empresa

app_name = 'empresa'

urlpatterns = [
    path('', lista_empresas, name='lista_empresas'),  # Aquí se usa 'lista_empresas'
    path('crear/', crear_empresa, name='crear_empresa'),
    path('actualizar/<int:pk>/', actualizar_empresa, name='actualizar_empresa'),
    path('eliminar/<int:pk>/', eliminar_empresa, name='eliminar_empresa'),
    path('detalle/<int:pk>/', views.empresa_detalle, name='detalle_empresa'),
]
