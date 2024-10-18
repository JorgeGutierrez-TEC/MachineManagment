# accounts/urls.py
from django.urls import path
from .views import CustomLoginView, admin_dashboard, empleado_dashboard, empresa_dashboard, home_dashboard, inventario_dashboard, maquinaria_dashboard, status_dashboard


urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('admin/', admin_dashboard, name='admin'),
    path('empleado/', empleado_dashboard, name='empleado'),
    path('empresa/', empresa_dashboard, name='empresa'),
    path('home/', home_dashboard, name='home'),
    path('inventario/', inventario_dashboard, name='inventario'),
    path('maquinaria/', maquinaria_dashboard, name='maquinaria'),
    path('status/', status_dashboard, name='status'),
    
]
