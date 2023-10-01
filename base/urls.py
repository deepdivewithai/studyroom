from django.urls import path
from base import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create-room/', views.createRoom, name='create-room'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
    path('update-room/<str:pk>/', views.updateRoom, name='update-room'),
]