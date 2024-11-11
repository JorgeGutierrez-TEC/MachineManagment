from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Piezas, InventarioPiezas, ProveedorPiezas, AddPieza
from django.views import generic
# Create your views here.



class Piezas(LoginRequiredMixin, generic.ListView):
    model = Piezas
    template_name = 'maquinaria/lista_piezas.html'
    login_url = "home:index"

class InventarioPiezas(LoginRequiredMixin, generic.ListView):
    model = InventarioPiezas
    template_name = 'maquinaria/lista_inventario.html'
    login_url = "home:index"

class Proveedores(LoginRequiredMixin, generic.ListView):
    model = ProveedorPiezas
    template_name = 'maquinaria/lista_proveedor.html'
    login_url = "home:index"