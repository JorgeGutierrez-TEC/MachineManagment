from django.urls import path

from maquinaria import views

app_name = "maquinaria"

urlpatterns = [
    path('', views.maquinaria.as_view(), name="maquinaria"),
]