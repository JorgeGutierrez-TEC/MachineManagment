from django import forms

from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=16, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe tu Username"})) 
    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={"type":"password", "class":"form-control", "placeholder":"Escribe tu Password"}))
    password2 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={"type":"password", "class":"form-control", "placeholder":"Confirma tu Password"}))  
    first_name = forms.CharField(max_length=16, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe tu First Name"})) 
    last_name = forms.CharField(max_length=16, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe tu Last Name"})) 
    email = forms.EmailField(max_length=32, widget=forms.EmailInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe tu Email"})) 
