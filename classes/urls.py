from django.urls import path, include

from . import views

urlpatterns = [
    path('classes', views.ClassList.as_view()),
    # path('class', views.ClassDetail.as_view()),
    path('class/<int:id>', views.ClassDetail.as_view()),
]