from django.urls import path, include

from . import views

urlpatterns = [
    path('base/subjects', views.SubjectList.as_view()),
    path('base/batches', views.BatchList.as_view()),
]