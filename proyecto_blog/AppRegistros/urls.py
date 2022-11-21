from django.contrib import admin
from django.urls import path
from AppRegistros import views

urlpatterns = [
    path('', views.mostrar_index,name='principal'),
    path('login/',views.mostrar_login,name='login'),
    path('registro/',views.RegistroView.as_view(),name='registro')
]