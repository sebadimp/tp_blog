from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Perfiles
from .forms import RegistroForm,UserUpdateForm,PerfilForm,AvatarForm




class RegistroView(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy('principal')
    template_name = "registro.html"

class AdminLoginView(LoginView):
    template_name='login.html'

class AdminLogoutView(LogoutView):
    template_name='logout.html'


@login_required
def add_avatar(request):

    if request.method == 'POST':

        miAvatar = AvatarForm(request.POST, request.FILES)

        if miAvatar.is_valid():

            usuario = request.user

            avatar = Perfiles.objects.filter(user=usuario)

            file = miAvatar.cleaned_data
            
            if len(avatar) > 0:

                avatar = avatar[0]
                avatar.imagen = file['imagen']
                avatar.save()

                avatar = Perfiles.objects.filter(user=request.user)

                imagen = avatar[0].imagen.url

            else:

                avatar = Perfiles(user=usuario, imagen=miAvatar.cleaned_data['imagen'])
                avatar.save()

                imagen = None



        #return render(request, 'AppBlog/post_list.html', {'imagen':imagen})
        return redirect('profile')
    else:

        miAvatar = AvatarForm()

        imagen = None
        
        return render(request, 'AppRegistros/user_avatar.html', {'miAvatar': miAvatar, 'imagen': imagen})

@login_required
def profile(request):
    
    user = request.user

    perfil = Perfiles.objects.filter(user=request.user)
    try:
        if len(perfil) > 0:

            imagenperfil = perfil[0].imagen.url
            sobremi = perfil[0].sobremi
            instagram = perfil[0].instagram
            facebook = perfil[0].facebook
            twitter = perfil[0].twitter

        else:

            imagenperfil = None
            sobremi = ""
            instagram = ""
            facebook = ""
            twitter = ""
    except:
            imagenperfil = None
            sobremi = perfil[0].sobremi
            instagram = perfil[0].instagram
            facebook = perfil[0].facebook
            twitter = perfil[0].twitter


    if request.user.username:

        perfilusuario = Perfiles.objects.filter(user=request.user)
        try:
            if len(perfilusuario) > 0:

                img = perfilusuario[0].imagen.url

            else:

                img = None
        except:
            img = None
    
    else:

        img = None

    return render(request, 'AppRegistros/user_profile.html', {'user':user, 'imagenperfil':imagenperfil, 'img': img, 'sobremi':sobremi, 'instagram':instagram, 'facebook':facebook, 'twitter':twitter})

@login_required
def edituser(request):

    usuario = request.user

    perfil = Perfiles.objects.filter(user=usuario)

    if len(perfil) > 0:
        
        imagenperfil = perfil[0].imagen.url

    else:

        imagenperfil= None

    if request.method == 'POST':
         
        usereditform = UserUpdateForm(request.POST)
        perfileditform = PerfilForm(request.POST)

        if usereditform.is_valid() and perfileditform.is_valid():

            info_usuario = usereditform.cleaned_data

            usuario.email = info_usuario["email"]
            usuario.first_name = info_usuario["first_name"]
            usuario.last_name = info_usuario["last_name"]
            usuario.password1 = info_usuario["password1"]
            usuario.password2 = info_usuario["password2"]

            usuario.save()

            usuario_perfil = Perfiles.objects.filter(user=usuario)
            info_perfil = perfileditform.cleaned_data

            if len(usuario_perfil) > 0:

                usuario_perfil = usuario_perfil[0]

                usuario_perfil.sobremi = info_perfil['sobremi']
                usuario_perfil.instagram = info_perfil['instagram']
                usuario_perfil.facebook = info_perfil['facebook']
                usuario_perfil.twitter = info_perfil['twitter']

                usuario_perfil.save()

            else:

                usuario_perfil = Perfiles(user= usuario, sobremi=info_perfil['sobremi'], instagram=info_perfil['instagram'], facebook=info_perfil['facebook'], twitter=info_perfil['twitter'])
                usuario_perfil.save()

            return redirect('profile')

        else:

            usereditform = UserUpdateForm()
            perfileditform = PerfilForm()

            return render(request, 'AppRegistros/user_update.html', {"usereditform": usereditform, "perfileditform":perfileditform, "errors": ['Datos ingresados inválidos.'], 'img':imagenperfil})

    else: 

        usereditform = UserUpdateForm(initial={'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
        perfileditform = PerfilForm()

        return render(request, 'AppRegistros/user_update.html', {"usereditform": usereditform, "perfileditform":perfileditform, "errors": ['Datos ingresados inválidos.'], 'img':imagenperfil})