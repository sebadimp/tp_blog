from django import forms
from django.contrib.auth.models import User
from .models import Avatar
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
 


class RegistroForm(UserCreationForm):
    username = forms.CharField(label='Usuario', min_length=5, max_length=150)  
    email = forms.EmailField(label='Email')  
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirmar password', widget=forms.PasswordInput)
    #first_name= forms.CharField(label='Nombre',max_length=100)
    #last_name= forms.CharField(label='Apellido',max_length=100)
    

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
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirmar password', widget=forms.PasswordInput)
    first_name= forms.CharField(label='Nombre',max_length=100)
    last_name= forms.CharField(label='Apellido',max_length=100)
    

    class Meta:
        model=User
        fields=[
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
        ]        


class UserInfoForm(forms.Form):

    biografia = forms.CharField(widget=forms.Textarea, label='Biografía', required=False)
    instagram = forms.URLField(required=False, label='Instagram')
    facebook = forms.URLField(required=False, label='Facebook')
    twitter = forms.URLField(required=False, label='Twitter')


class AvatarForm(forms.Form):
    imagen=forms.ImageField()

class AvatarAddForm(ModelForm):
    class Meta:
        model = Avatar
        fields = ('user','imagen')
        widgets = {
            'user': forms.HiddenInput,
        }