from django.contrib import admin
from django.urls import path
from AppRegistros import views

urlpatterns = [
    path('avatar/', views.avatar,name='avatar'),
    path('registro/',views.RegistroView.as_view(),name='registro'),
    path('login/',views.AdminLoginView.as_view(),name='login'),
    path('logout/',views.AdminLogoutView.as_view(),name='logout'),
    path('user_update/',views.UserUpdate,name='user update'),  
    path('user_profile/<pk>',views.UserProfile.as_view(),name='profile'),
    path('user_avatar/',views.AvatarAdd.as_view(),name='add avatar'),
    path('avatar_update/<pk>',views.AvatarUpdate.as_view(),name='update avatar'),
]