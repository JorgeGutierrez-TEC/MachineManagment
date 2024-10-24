from django.db import models

class Status(models.Model):
    id = models.AutoField(primary_key=True)  # Clave primaria autoincremental
    name = models.CharField(max_length=50)  # Nombre del estado
    description = models.CharField(max_length=200, blank=True, null=True)  # Descripción opcional del estado
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de la última actualización
    is_active = models.BooleanField(default=True)  # Indica si el estado está activo
    is_deleted = models.BooleanField(default=False)  # Indica si el estado está eliminado

    def __str__(self):
        return self.name
