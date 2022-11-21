from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from AppBlog import urls
from .forms import RegistroForm

def mostrar_index(request):

    return render(request,'index.html')


class RegistroView(CreateView):

    form_class = RegistroForm
    success_url = reverse_lazy('principal')
    template_name = "registro.html"

def mostrar_login(request):

    return render(request,'login.html')