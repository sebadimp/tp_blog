from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.core.paginator import Paginator

from .models import Post


def mostrar_index(request):
    return render(request,'index.html')



class PostList(ListView):
    model= Post
    success_url = '/'
    paginate_by = 5
    template_name= 'AppBlog/post_list.html'

    def get_queryset(self):
        return Post.objects.all().order_by('-id').values()


class PostListCuidados(ListView):
    model= Post    
    paginate_by = 5
    template_name= 'AppBlog/post_filter_cuidados.html'
    
    def get_queryset(self):
        return Post.objects.filter(categoria__iexact='Cuidados').order_by('-id').values()

class PostListAlimentación(ListView):
    model= Post    
    paginate_by = 5
    template_name= 'AppBlog/post_filter_alimentacion.html'

    def get_queryset(self):
        return Post.objects.filter(categoria__iexact='Alimentación').order_by('-id').values()
    

class PostListEntretenimiento(ListView):
    model= Post    
    paginate_by = 5
    template_name= 'AppBlog/post_filter_entretenimiento.html'

    def get_queryset(self):
        return Post.objects.filter(categoria__iexact='Entretenimiento').order_by('-id').values()



class PostCreate(CreateView):
    model = Post
    template_name = 'AppBlog/post_create.html'
    success_url = '/'
    fields=['titulo','subtitulo','categoria','contenido','fecha','autor']

class PostDetail(DetailView):
    model = Post
    template_name = 'AppBlog/post_detail.html'


class PostDelete(DeleteView):
    model=Post
    template_name='AppBlog/post_delete.html'
    success_url = '/'

class PostUpdate(UpdateView):
    model=Post
    template_name = 'AppBlog/post_create.html'
    success_url="/"
    fields=['titulo','subtitulo','categoria','contenido','fecha','autor']



