from django.urls import path, include

from user import views

urlpatterns = [
    path('profile', views.ProfileDetail.as_view()),
    
]