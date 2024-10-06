from django.urls import path

from empresa import views

app_name = "empresa"

urlpatterns = [
    path('', views.empresa.as_view(), name="empresa"),
]