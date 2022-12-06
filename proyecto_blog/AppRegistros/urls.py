from django.contrib import admin
from django.urls import path
from AppRegistros import views

urlpatterns = [
    path('registro/',views.RegistroView.as_view(),name='registro'),
    path('login/',views.AdminLoginView.as_view(),name='login'),
    path('logout/',views.AdminLogoutView.as_view(),name='logout'),
    path('add_avatar/',views.add_avatar,name='add avatar'),
    path('user_profile/',views.profile,name='profile'),
    path('edit_user/',views.edituser,name='edit user'),
    
]