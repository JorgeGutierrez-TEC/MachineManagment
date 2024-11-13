from django.urls import path

from empleados import views

app_name = "empleados"

urlpatterns = [
  path('', views.EmpleadosView.as_view(), name="empleados"),
    path('list/', views.EmpleadosListView.as_view(), name="empleado_list"),
    path('<int:pk>/detalles/', views.EmpleadosDetailView.as_view(), name="ver_empleado"),
    path('<int:pk>/editar/', views.EmpleadosUpdateView.as_view(), name="actualizar_empleado"),
    path('<int:pk>/eliminar/', views.EmpleadosDeleteView.as_view(), name="eliminar_empleado"),
]