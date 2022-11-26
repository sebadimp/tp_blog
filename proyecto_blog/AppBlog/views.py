from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Post


def mostrar_indexprincipal(request):
    return render(request,'indexprincipal.html')


class PostList(LoginRequiredMixin,ListView):
    model= Post
    success_url = '/post_list'
    paginate_by = 6
    template_name= 'AppBlog/post_list.html'

    def get_queryset(self):
        return Post.objects.all().order_by('-id').values()


class PostListCuidados(LoginRequiredMixin,ListView):
    model= Post    
    paginate_by = 5
    template_name= 'AppBlog/post_filter_cuidados.html'
    
    def get_queryset(self):
        return Post.objects.filter(categoria__iexact='Cuidados').order_by('-id').values()

class PostListAlimentación(LoginRequiredMixin,ListView):
    model= Post    
    paginate_by = 5
    template_name= 'AppBlog/post_filter_alimentacion.html'

    def get_queryset(self):
        return Post.objects.filter(categoria__iexact='Alimentación').order_by('-id').values()
    

class PostListEntretenimiento(LoginRequiredMixin,ListView):
    model= Post    
    paginate_by = 5
    template_name= 'AppBlog/post_filter_entretenimiento.html'

    def get_queryset(self):
        return Post.objects.filter(categoria__iexact='Entretenimiento').order_by('-id').values()



class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'AppBlog/post_create.html'
    success_url = '/post_list'
    fields=['titulo','subtitulo','categoria','contenido','fecha','autor']

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
    fields=['titulo','subtitulo','categoria','contenido','fecha','autor']


class ControlUsuarios(LoginRequiredMixin,ListView):
    model= User
    success_url = '/indexusuarios'
    template_name= 'AppBlog/user_list.html'

    def get_queryset(self):
        return User.objects.all().order_by('-id').values()
    
