from django import forms
from .models import Post
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ('idautor','titulo','descripcion','categoria','contenido','autor','imagen')
        widgets = {
            'idautor': forms.HiddenInput,
        }
    


