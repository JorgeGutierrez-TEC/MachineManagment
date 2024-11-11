from django.urls import path
from maquinaria import views

app_name = "maquinaria"

urlpatterns = [
    path('', views.MaquinariaView.as_view(), name="maquinaria"),
    path('list/', views.MaquinariaListView.as_view(), name="maquinaria_list"),
    path('<int:pk>/detalles/', views.MaquinariaDetailView.as_view(), name="ver_maquinaria"),
    path('<int:pk>/editar/', views.MaquinariaUpdateView.as_view(), name="actualizar_maquinaria"),
    path('<int:pk>/eliminar/', views.MaquinariaDeleteView.as_view(), name="eliminar_maquinaria"),

    path('tipo/crear/', views.CrearTipoMantenimiento.as_view(), name='crear_tipo_mantenimiento'),
    path('tipo/lista/', views.ListaTiposMantenimiento.as_view(), name='lista_tipomantenimiento'),
    path('crear/', views.CrearMantenimiento.as_view(), name='crear_mantenimiento'),
    path('lista/', views.ListaMantenimientos.as_view(), name='Lista_mantenimiento'),
    path('tipo/actualizar/<int:pk>/', views.ActualizarTipoMantenimiento.as_view(), name='actualizar_tipo_mantenimiento'),
    path('tipo/eliminar/<int:pk>/', views.EliminarTipoMantenimiento.as_view(), name='eliminar_tipo_mantenimiento'),
    path('actualizar/<int:pk>/', views.ActualizarMantenimiento.as_view(), name='actualizar_mantenimiento'),
    path('eliminar/<int:pk>/', views.EliminarMantenimiento.as_view(), name='eliminar_mantenimiento'),
]
