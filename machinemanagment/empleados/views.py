from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Empleados
from .forms import EmpleadoForm  

# Vista para la creación de un empleado
class EmpleadosView(generic.View):
    template_name = "empleados/empleados.html"

    def get(self, request):
        form = EmpleadoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleados:empleados')  # Redirige a la lista de empleados
        else:
            print(form.errors)  # Imprime los errores si el formulario no es válido
        return render(request, self.template_name, {'form': form})

# Vista para la lista de empleados
class EmpleadosListView(generic.ListView):
    model = Empleados
    template_name = "empleados/empleado_list.html"
    context_object_name = "empleados"

# Vista para los detalles de un empleado
class EmpleadosDetailView(generic.DetailView):
    model = Empleados
    template_name = "empleados/empleado_detail.html"
    context_object_name = "empleado"

# Vista para editar un empleado
class EmpleadosUpdateView(generic.UpdateView):
    model = Empleados
    form_class = EmpleadoForm  
    template_name = "empleados/empleado_form.html"

    def get_success_url(self):
        return reverse_lazy('empleados:empleado_list')  # Redirige a la lista de empleados

# Vista para eliminar un empleado
class EmpleadosDeleteView(generic.DeleteView):
    model = Empleados
    template_name = "empleados/empleado_confirm_delete.html"
    success_url = reverse_lazy('empleados:empleado_list')  # Redirige a la lista de empleados
