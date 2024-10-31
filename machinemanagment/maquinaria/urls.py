from django.urls import path

from maquinaria import views

app_name = "maquinaria"

urlpatterns = [
    path('', views.MaquinariaView.as_view(), name="maquinaria"),
    path('list/', views.MaquinariaListView.as_view(), name="maquinaria_list"),

]