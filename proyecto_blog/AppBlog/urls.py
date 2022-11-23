"""proyecto_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppBlog import views

urlpatterns = [
    path('index/', views.mostrar_index,name='principal'),
    path('',views.PostList.as_view(),name='post list'),
    path('post_create/',views.PostCreate.as_view(),name='post create'),
    path('post_filter=cuidados/',views.PostListCuidados.as_view(),name='filtro cuidados'),
    path('post_filter=alimentacion/',views.PostListAlimentación.as_view(),name='filtro alimentacion'),
    path('post_filter=entretenemiento/',views.PostListEntretenimiento.as_view(),name='filtro entretenimiento'),
    path('post_detail/<pk>',views.PostDetail.as_view(),name='post detail'),
    path('post_delete/<pk>',views.PostDelete.as_view(),name='post delete'),
    path('post_update/<pk>',views.PostUpdate.as_view(),name='post update'),
    
    
]