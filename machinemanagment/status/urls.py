from django.urls import path

from status import views

app_name = "status"

urlpatterns = [
    path('', views.status.as_view(), name="status"),
]