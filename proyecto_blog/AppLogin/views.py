from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView

class AdminLoginView(LoginView):
    template_name='AppLogin/login.html'