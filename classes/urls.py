from django.urls import path, include

from . import views

urlpatterns = [
    path('classes', views.ClassList.as_view()),
    path('class', views.ClassDetail.as_view()),
    path('class/<int:id>', views.ClassDetail.as_view()),
    path('class/students/<int:id>', views.StudentListClass.as_view()),
    path('class/student/<int:c_id>/<int:s_id>', views.AddRemoveStudentClass.as_view()),
]