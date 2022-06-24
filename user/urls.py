from django.urls import path, include

from user import views

urlpatterns = [
    path('profile', views.ProfileDetail.as_view()),
    path('students', views.StudentList.as_view()),
    path('students/csv', views.CreateStudentsCSV.as_view()),
]