from django.urls import path

from home import views

app_name = "home"

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('logout/', views.LogOut.as_view(), name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
]