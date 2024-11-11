from django.urls import path

from administrador import views

app_name = "administrador"

urlpatterns = [
    path('', views.administrador.as_view(), name="Areas"),
]