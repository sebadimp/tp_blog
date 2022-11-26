from django.contrib import admin
from django.urls import path
from AppRegistros import views

urlpatterns = [
    #path('', views.mostrar_index,name='principal'),
    path('registro/',views.RegistroView.as_view(),name='registro'),
    path('login/',views.AdminLoginView.as_view(),name='login'),
    path('logout/',views.AdminLogoutView.as_view(),name='logout'),
]