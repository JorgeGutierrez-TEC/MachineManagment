from django.urls import path
from maquinaria import views

app_name = "maquinaria"

urlpatterns = [
    path('', views.MaquinariaView.as_view(), name="maquinaria"),
    path('list/', views.MaquinariaListView.as_view(), name="maquinaria_list"),
    path('<int:pk>/detalles/', views.MaquinariaDetailView.as_view(), name="ver_maquinaria"),
    path('<int:pk>/editar/', views.MaquinariaUpdateView.as_view(), name="actualizar_maquinaria"),
    path('<int:pk>/eliminar/', views.MaquinariaDeleteView.as_view(), name="eliminar_maquinaria"),
]
