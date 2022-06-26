from django.urls import path, include

from user import views

urlpatterns = [
    path('profile', views.ProfileDetail.as_view()),
    path('student/<int:sid>', views.StudentDetail.as_view()),
    path('students', views.StudentList.as_view()),
    path('teachers', views.TeacherList.as_view()),
    path('students/csv', views.CreateStudentsCSV.as_view()),
    path('password', views.ChangePassword.as_view()),
    path('profilepicture', views.ChangeProfileImage.as_view()),
]