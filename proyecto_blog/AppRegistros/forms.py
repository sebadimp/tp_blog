from django import forms
from django.contrib.auth.models import User
from .models import Perfiles
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
 

class RegistroForm(UserCreationForm):
    username = forms.CharField(label='Usuario', min_length=5, max_length=150)  
    email = forms.EmailField(label='Email')  
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'password1',
            'password2',
        ]

class UserUpdateForm(UserCreationForm):
    email = forms.EmailField(label='Email')  
    password1 = forms.CharField(label='Nuevo contraseña', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    first_name= forms.CharField(label='Nombre',max_length=100,required=False)
    last_name= forms.CharField(label='Apellido',max_length=100,required=False)
    

    class Meta:
        model=User        
        fields=[
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
        ]        
        help_text = {k: "" for k in fields}


class AvatarForm(forms.Form):
    imagen=forms.ImageField()


class PerfilForm(forms.Form):
    sobremi = forms.CharField(widget=forms.Textarea, label='Sobre mi', required=False)
    instagram = forms.URLField(required=False, label='Instagram')
    facebook = forms.URLField(required=False, label='Facebook')
    twitter = forms.URLField(required=False, label='Twitter')

