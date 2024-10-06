from django.shortcuts import render
from django.views import generic
# Create your views here.


class inventario(generic.View):
    template_name = "inventario/inventario.html"
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)