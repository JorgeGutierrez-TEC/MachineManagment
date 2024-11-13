from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Status, BancoEm
from .forms import StatusForm, BancoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Ganancias, Reparaciones
from django.db.models import Sum
from datetime import datetime
from django.shortcuts import redirect


# Create
class CreateStatus(LoginRequiredMixin, generic.CreateView):
    template_name = "status/status_create.html"
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy("status:status_list")
    login_url = "home:index"

# List
class ListStatus(LoginRequiredMixin, generic.View):
    template_name = "status/status_list.html"
    context = {}
    login_url = "home:index"

    def get(self, request):
        self.context = {
            "statuses": Status.objects.filter(is_deleted=False)  # Solo estados no eliminados
        }
        return render(request, self.template_name, self.context)

# Detail
class DetailStatus(LoginRequiredMixin, generic.View):
    template_name = "status/status_detail.html"
    context = {}
    login_url = "home:index"

    def get(self, request, pk):
        status = get_object_or_404(Status, pk=pk)
        self.context = {
            "status": status
        }
        return render(request, self.template_name, self.context)

# Update
class UpdateStatus(LoginRequiredMixin, generic.UpdateView):
    template_name = "status/status_update.html"
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy("status:status_list")
    login_url = "home:index"

# Delete
class DeleteStatus(LoginRequiredMixin, generic.DeleteView):
    template_name = "status/status_delete.html"
    model = Status
    success_url = reverse_lazy("status:status_list")
    login_url = "home:index"
    
    def post(self, request, *args, **kwargs):
        status = self.get_object()
        status.is_deleted = True  # Cambiar is_deleted a True en lugar de eliminar el objeto
        status.save()
        return redirect(self.success_url)

from datetime import datetime
from django.shortcuts import render
from django.db.models import Sum
from .models import Ganancias, Reparaciones  # Asegúrate de que estos modelos estén importados correctamente

def graficas_view(request):
    # Datos de ganancias
    ganancias = Ganancias.objects.values('fecha').annotate(total_ingresos=Sum('ingresos')).order_by('fecha')
    fechas_ganancias = [g['fecha'].strftime('%Y-%m-%d') for g in ganancias]
    ingresos = [g['total_ingresos'] for g in ganancias]

    # Datos de reparaciones del mes actual
    inicio_mes = datetime.now().replace(day=1)
    reparaciones = Reparaciones.objects.filter(fecha_reparacion__gte=inicio_mes).count()  # Cambiado a 'fecha_reparacion'

    context = {
        'fechas_ganancias': fechas_ganancias,
        'ingresos': ingresos,
        'reparaciones': reparaciones,
    }
    return render(request, 'status/graficas.html', context)
#Banco
class BancoView(generic.View):
    template_name = "status/banco.html"
    
    def get(self, request):
        form = BancoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BancoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('status:banco')  
        else:
            print(form.errors)  # Imprime los errores si el formulario no es válido
        return render(request, self.template_name, {'form': form})

class BancoListView(generic.ListView):
    model = BancoEm
    template_name = "status/bancoem_list.html"
    context_object_name = "bancos"

class BancoDetailView(generic.DetailView):
    model = BancoEm
    template_name = "status/banco_detail.html"
    context_object_name = "banco"

class BancoUpdateView(generic.UpdateView):
    model = BancoEm
    form_class = BancoForm
    template_name = "status/banco_form.html"

    def get_success_url(self):
        return reverse_lazy('status:bancoem_list')

class BancoDeleteView(generic.DeleteView):
    model = BancoEm
    template_name = "status/banco_confirm_delete.html"
    success_url = reverse_lazy('status:bancoem_list')