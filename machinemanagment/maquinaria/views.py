from django.shortcuts import render, redirect
from django.views import generic
from .forms import MaquinariaForm
from .models import Maquinaria
from django.db import transaction

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