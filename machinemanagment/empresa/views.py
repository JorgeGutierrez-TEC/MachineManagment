from django.shortcuts import render
from django.views import generic
# Create your views here.


class empresa(generic.View):
    template_name = "empresa/empresa.html"
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)