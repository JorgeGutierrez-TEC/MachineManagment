from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from home.forms import SignUpForm
# Create your views here.


class Index(generic.View):
    template_name = "home/index.html"
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home:index")
        else:
            return redirect("home:index")


class LogOut(generic.View):
    def get(self, request):
        logout(request)
        return redirect("home:index")
    
class SignUp(generic.CreateView):
    template_name = "home/signup.html"
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy("home:index")

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect("home:index")
        else:
            return redirect("home:index")