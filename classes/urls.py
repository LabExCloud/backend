from django.urls import path, include

from . import views

urlpatterns = [
    path('classes', views.ClassList.as_view()),
]