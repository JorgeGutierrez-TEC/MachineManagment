from django.urls import path
from .views import CreateStatus, ListStatus, DetailStatus, UpdateStatus, DeleteStatus

app_name = 'status'

urlpatterns = [
    path('status/create/', CreateStatus.as_view(), name='status_create'),
    path('status/', ListStatus.as_view(), name='status_list'),
    path('status/<int:pk>/', DetailStatus.as_view(), name='status_detail'),
    path('status/update/<int:pk>/', UpdateStatus.as_view(), name='status_update'),
    path('status/delete/<int:pk>/', DeleteStatus.as_view(), name='status_delete'),
]
