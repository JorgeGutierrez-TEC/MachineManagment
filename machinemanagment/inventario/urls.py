from django.urls import path

from inventario import views

app_name = "inventario"

urlpatterns = [
    path('', views.inventario.as_view(), name="inventario"),
]