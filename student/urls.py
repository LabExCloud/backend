from django.urls import path

from . import views

urlpatterns = [
    path('exam/', views.exam, name='exam'),
    path('lab/', views.lab, name='lab'),
    path('profile/', views.profile, name='profile'),
    path('resources/', views.resources, name='resources'),
]