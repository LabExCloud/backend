from django.urls import path, include

from resources import views

urlpatterns = [
    path('resources', views.ResourceList.as_view()),
    path('resources/<int:sem>', views.ResourceListSem.as_view()),
]