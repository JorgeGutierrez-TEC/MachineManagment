from django.urls import path

from empleados import views

app_name = "empleados"

urlpatterns = [
    path('', views.empleados.as_view(), name="empleados"),
]