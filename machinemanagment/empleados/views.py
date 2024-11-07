from django.shortcuts import render
from django.views import generic
# Create your views here.


class empleados(generic.View):
    template_name = "empleados/empleados.html"
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)