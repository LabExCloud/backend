from django.urls import path, include

from user import views

urlpatterns = [
    path('profile/<str:username>', views.ProfileDetail.as_view()),
    
]