from django.shortcuts import render
from django.views import generic
# Create your views here.


class Index(generic.View):
    template_name = "home/index.html"
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)