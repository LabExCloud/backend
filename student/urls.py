from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('exam/', views.exam, name='exam'),
    path('lab/', views.lab, name='lab'),
    path('profile/', views.profile, name='profile'),
    path('resources/', views.resources, name='resources'),
    path('login/', auth_views.LoginView.as_view(template_name='student/login.html'), name='login'),
]