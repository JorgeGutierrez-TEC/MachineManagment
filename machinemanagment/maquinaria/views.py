from django.shortcuts import render, redirect
from django.views import generic
from .forms import MaquinariaForm, MantenimientoForm, TipoMantenimientoForm
from .models import Maquinaria, Mantenimientos, TipoMantenimiento
from django.urls import reverse_lazy
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin


class MaquinariaView(generic.View):
    template_name = "maquinaria/maquinaria.html"
    
    def get(self, request):
        form = MaquinariaForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = MaquinariaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maquinaria:maquinaria')  # Redirige a la misma vista o a otra que desees
        else:
            print(form.errors)  # Imprime los errores si el formulario no es válido
        return render(request, self.template_name, {'form': form})

class MaquinariaListView(generic.ListView):
    model = Maquinaria
    template_name = "maquinaria/maquinaria_list.html"
    context_object_name = "maquinarias"

class MaquinariaDetailView(generic.DetailView):
    model = Maquinaria
    template_name = "maquinaria/maquinaria_detail.html"
    context_object_name = "maquinaria"

class MaquinariaUpdateView(generic.UpdateView):
    model = Maquinaria
    form_class = MaquinariaForm
    template_name = "maquinaria/maquinaria_form.html"

    def get_success_url(self):
        return reverse_lazy('maquinaria:maquinaria_list')

class MaquinariaDeleteView(generic.DeleteView):
    model = Maquinaria
    template_name = "maquinaria/maquinaria_confirm_delete.html"
    success_url = reverse_lazy('maquinaria:maquinaria_list')


class CrearTipoMantenimiento(generic.CreateView):
    model = TipoMantenimiento
    form_class = TipoMantenimientoForm
    template_name = 'maquinaria/crear_tipo_mantenimiento.html'
    success_url = reverse_lazy("maquinaria:lista_tipomantenimiento")
    login_url = "home:index"

class ListaTiposMantenimiento(LoginRequiredMixin, generic.ListView):
    model = TipoMantenimiento
    template_name = 'maquinaria/lista_tipomantenimiento.html'
    login_url = "home:index"

class CrearMantenimiento(LoginRequiredMixin, generic.CreateView):
    model = Mantenimientos
    form_class = MantenimientoForm
    template_name = 'maquinaria/crear_mantenimiento.html'
    success_url = reverse_lazy('maquinaria:Lista_mantenimiento')
    login_url = "home:index"

class ListaMantenimientos(LoginRequiredMixin, generic.ListView):
    model = Mantenimientos
    template_name = 'maquinaria/Lista_mantenimiento.html'
    login_url = "home:index"

class ActualizarTipoMantenimiento(LoginRequiredMixin, generic.UpdateView):
    model = TipoMantenimiento
    form_class = TipoMantenimientoForm
    template_name = 'maquinaria/actualizar_tipo_mantenimiento.html'
    success_url = reverse_lazy('maquinaria:lista_tipomantenimiento')
    login_url = "home:index"

class EliminarTipoMantenimiento(LoginRequiredMixin, generic.DeleteView):
    model = TipoMantenimiento
    template_name = 'maquinaria/eliminar_tipo_mantenimiento.html'
    success_url = reverse_lazy('maquinaria:lista_tipomantenimiento')
    login_url = "home:index"


class ActualizarMantenimiento(LoginRequiredMixin, generic.UpdateView):
    model = Mantenimientos
    form_class = MantenimientoForm
    template_name = 'maquinaria/actualizar_mantenimiento.html'
    success_url = reverse_lazy('maquinaria:Lista_mantenimiento')
    login_url = "home:index"

class EliminarMantenimiento(LoginRequiredMixin, generic.DeleteView):
    model = Mantenimientos
    template_name = 'maquinaria/eliminar_mantenimiento.html'
    success_url = reverse_lazy('maquinaria:Lista_mantenimiento')
    login_url = "home:index"


