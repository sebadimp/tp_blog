from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User
from AppBlog.forms import *
from .models import Post


def mostrar_indexprincipal(request):
    return render(request,'indexprincipal.html')

def sobremi(request):
    return render(request,'AppBlog/sobremi.html')

class PostList(LoginRequiredMixin,ListView):
    model= Post
    success_url = '/post_list'
    paginate_by = 6
    template_name= 'AppBlog/post_list.html'

    def get_queryset(self):
        return Post.objects.all().order_by('-fecha_creacion').values()


class PostListCuidados(LoginRequiredMixin,ListView):
    model= Post    
    paginate_by = 6
    template_name= 'AppBlog/post_filter_cuidados.html'
    
    def get_queryset(self):
        return Post.objects.filter(categoria__iexact='Cuidados').order_by('-fecha_creacion').values()

class PostListAlimentación(LoginRequiredMixin,ListView):
    model= Post    
    paginate_by = 6
    template_name= 'AppBlog/post_filter_alimentacion.html'

    def get_queryset(self):
        return Post.objects.filter(categoria__iexact='Alimentación').order_by('-fecha_creacion').values()
    

class PostListEntretenimiento(LoginRequiredMixin,ListView):
    model= Post    
    paginate_by = 6
    template_name= 'AppBlog/post_filter_entretenimiento.html'

    def get_queryset(self):
        return Post.objects.filter(categoria__iexact='Entretenimiento').order_by('-fecha_creacion').values()

class PostListEnfermedades(LoginRequiredMixin,ListView):
    model= Post    
    paginate_by = 6
    template_name= 'AppBlog/post_filter_enfermedades.html'

    def get_queryset(self):
        return Post.objects.filter(categoria__iexact='Enfermedades').order_by('-fecha_creacion').values()

class PostListLugares(LoginRequiredMixin,ListView):
    model= Post    
    paginate_by = 6
    template_name= 'AppBlog/post_filter_lugares.html'

    def get_queryset(self):
        return Post.objects.filter(categoria__iexact='Lugares_y_Paseos').order_by('-fecha_creacion').values()

class PostListCuriosidades(LoginRequiredMixin,ListView):
    model= Post    
    paginate_by = 6
    template_name= 'AppBlog/post_filter_curiosidades.html'

    def get_queryset(self):
        return Post.objects.filter(categoria__iexact='Curiosidades').order_by('-fecha_creacion').values()

class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'AppBlog/post_create.html'
    success_url = '/post_list'
    #fields=['idautor','titulo','descripcion','categoria','contenido','fecha','autor','imagen']
    form_class=PostCreateForm
    
    def get_initial(self):
        return {'autor': self.request.user,'idautor':self.request.user}

class PostDetail(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'AppBlog/post_detail.html'


class PostDelete(LoginRequiredMixin,DeleteView):
    model=Post
    template_name='AppBlog/post_delete.html'
    success_url = '/post_list'

class PostUpdate(LoginRequiredMixin,UpdateView):
    model=Post
    template_name = 'AppBlog/post_create.html'
    success_url="/post_list"
    fields=['titulo','descripcion','categoria','contenido','imagen']

@login_required
def buscar_titulo(request):

    if request.GET.get('titulo',False):
        titulo=request.GET['titulo']
        posteos=Post.objects.filter(titulo__icontains=titulo)

        return render(request,'AppBlog/post_list.html',{'posteos':posteos})

    else:
        respuesta="No hay resultados"

    return render(request,'AppBlog/post_list.html',{'respuesta':respuesta})
