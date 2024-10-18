from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

# Definición de usuarios, contraseñas y roles
USER_CREDENTIALS = {
    'admin_user': {'password': 'adminpass', 'role': 'admin'},
    'empleado_user': {'password': 'empleadopass', 'role': 'empleado'},
    'empresa_user': {'password': 'empresapass', 'role': 'empresa'},
    'home_user': {'password': 'homepass', 'role': 'home'},
    'inventario_user': {'password': 'inventariopass', 'role': 'inventario'},
    'maquinaria_user': {'password': 'maquinariapass', 'role': 'maquinaria'},
    'status_user': {'password': 'statuspass', 'role': 'status'},
}

class CustomLoginView(View):
    def get(self, request):
        return render(request, 'login/login.html')  # Renderiza el formulario de inicio de sesión

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verificación de credenciales
        if username in USER_CREDENTIALS:
            user_data = USER_CREDENTIALS[username]
            if user_data['password'] == password:
                role = user_data['role']
                # Redirigir según el rol
                if role == 'admin':
                    return redirect('admin')  # Cambia esto por la URL del admin
                elif role == 'empleado':
                    return redirect('empleado')  # Cambia esto por la URL del empleado
                elif role == 'empresa':
                    return redirect('empresa')  # Cambia esto por la URL de la empresa
                elif role == 'home':
                    return redirect('home')  # Cambia esto por la URL de home
                elif role == 'inventario':
                    return redirect('inventario')  # Cambia esto por la URL del inventario
                elif role == 'maquinaria':
                    return redirect('maquinaria')  # Cambia esto por la URL de maquinaria
                
                elif role == 'status':
                    return redirect('status')  # Cambia esto por la URL del estado
            else:
                messages.error(request, 'Credenciales incorrectas. Inténtalo de nuevo.')
        else:
            messages.error(request, 'Credenciales incorrectas. Inténtalo de nuevo.')

        return render(request, 'login/login.html')  # Muestra el formulario de inicio de sesión de nuevo

# Vistas para los dashboards

def admin_dashboard(request):
    return render(request, 'templates/admin/admin.html')

def empleado_dashboard(request):
    return render(request, 'templates/empleado/empleado.html')

def empresa_dashboard(request):
    return render(request, 'templates/empresa/empresa.html')

def home_dashboard(request):
    return render(request, 'templates/home/home.html')

def inventario_dashboard(request):
    return render(request, 'templates/inventario/inventario.html')

def maquinaria_dashboard(request):
    return render(request, 'templates/maquinaria/maquinaria.html')

def status_dashboard(request):
    return render(request, 'templates/templates/status/status.html')
