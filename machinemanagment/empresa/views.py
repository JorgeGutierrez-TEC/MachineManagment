from django.shortcuts import render, redirect, get_object_or_404
from .models import Empresas
from .forms import EmpresaForm

def lista_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresa/lista_empresas.html', {'empresas': empresas})

def crear_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige usando el namespace 'empresa'
            return redirect('empresa:lista_empresas')
    else:
        form = EmpresaForm()
    return render(request, 'empresa/crear_empresa.html', {'form': form})

def actualizar_empresa(request, pk):
    # Obtener la empresa por su ID
    empresa = get_object_or_404(Empresa, pk=pk)
    
    if request.method == 'POST':
        # Crear el formulario con los datos enviados y la instancia de la empresa
        form = EmpresaForm(request.POST, instance=empresa)
        
        if form.is_valid():
            # Guardar los cambios en la base de datos
            form.save()
            # Redirigir a la lista de empresas usando el namespace
            return redirect('empresa:lista_empresas')  # Asegúrate de incluir el namespace
    else:
        # Si no es una solicitud POST, crear un formulario vacío para la empresa
        form = EmpresaForm(instance=empresa)
    
    # Renderizar la plantilla con el formulario
    return render(request, 'empresa/actualizar_empresa.html', {'form': form})

def eliminar_empresa(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        empresa.delete()
        return redirect('empresa:lista_empresas')  # Asegúrate de usar el namespace correcto
    return render(request, 'empresa/eliminar_empresa.html', {'empresa': empresa})

def empresa_detalle(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    return render(request, 'empresa/empresa_detalle.html', {'empresa': empresa})
