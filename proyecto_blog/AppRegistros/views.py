from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Personal,Avatar
from .forms import RegistroForm,UserUpdateForm,UserInfoForm,AvatarForm,AvatarAddForm
from django.views.generic.detail import DetailView



class RegistroView(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy('principal')
    template_name = "registro.html"

class AdminLoginView(LoginView):
    template_name='login.html'

class AdminLogoutView(LogoutView):
    template_name='logout.html'

def UserUpdate(request):
    usuario = request.user
    
    if request.method == 'POST':
            
            edituserform = UserUpdateForm(request.POST)
            aboutuserform = UserInfoForm(request.POST)

            if edituserform.is_valid() and aboutuserform.is_valid():

                data = edituserform.cleaned_data

                usuario.email = data["email"]
                usuario.first_name = data["first_name"]
                usuario.last_name = data["last_name"]
                usuario.password1 = data["password1"]
                usuario.password2 = data["password2"]

                usuario.save()

                usuario_k = Personal.objects.filter(user=usuario)
                data1 = aboutuserform.cleaned_data

                if len(usuario_k) > 0:

                    usuario_k = usuario_k[0]

                    usuario_k.biografia = data1['biografia']
                    usuario_k.instagram = data1['instagram']
                    usuario_k.facebook = data1['facebook']
                    usuario_k.twitter = data1['twitter']

                    usuario_k.save()

                else:

                    usuario_k = Personal(user= usuario, biografia=data1['biografia'], instagram=data1['instagram'], facebook=data1['facebook'], twitter=data1['twitter'])
                    usuario_k.save()

                return redirect('post list')

            else:

                edituserform = UserUpdateForm()
                aboutuserform = UserInfoForm()

                return render(request, 'AppRegistros/user_update.html', {"edituserform": edituserform, "aboutuserform":aboutuserform, "errors": ['Datos ingresados inválidos.']})
                
    else: 

        edituserform = UserUpdateForm(initial={'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
        aboutuserform = UserInfoForm()

        return render(request, 'AppRegistros/user_update.html', {"aboutuserform":aboutuserform, "edituserform": edituserform})


class UserProfile(LoginRequiredMixin,DetailView):
    model = User
    template_name = 'AppRegistros/user_profile.html'


def agregaravatar(request):
    if request.method=='POST':

        avatar_form=AvatarForm(request.POST,request.FILES)

        if avatar_form.is_valid():
            

            usuario=User.objects.get(username=request.user)

           
            avatars= Avatar(user=usuario,imagen=avatar_form.cleaned_data['imagen'])

            avatars.save()

            return render(request,'AppRegistros/user_profile.html')
    
    else:

        avatar_form=AvatarForm()

    return render(request,'AppRegistros/user_avatar.html',{'avatar_form':avatar_form})

def avatar(request):
    avatars=Avatar.objects.filter(user=request.user.id)
    return render(request,'AppRegistros/indexuser.html',{'url':avatars[0].imagen.url})


class UserProfile(LoginRequiredMixin,DetailView):
    model = Avatar
    template_name = 'AppRegistros/user_profile.html'

class AvatarAdd(LoginRequiredMixin,CreateView):
    model = Avatar
    template_name = 'AppRegistros/user_avatar.html'
    success_url = reverse_lazy('post list')
    form_class=AvatarAddForm
    
    def get_initial(self):
        return {'user': self.request.user}

class AvatarUpdate(LoginRequiredMixin,UpdateView):
    model= Avatar
    template_name = 'AppRegistros/user_avatar.html'
    success_url =reverse_lazy('post list')
    fields=['imagen']

