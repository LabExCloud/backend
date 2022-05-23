from django.urls import path, include

from . import views

urlpatterns = [
    path('labexams/<int:id>', views.LabExamsList.as_view()),            # list all exams in a class id
    path('labexams/exam/<int:id>', views.LabExamDetail.as_view()),      # get details of exam id
    path('labexams/question/<int:id>', views.LabExamQuestionDetail.as_view()),
    path('labexams/question', views.LabExamQuestionDetail.as_view()),
    path('labexams/testcase/<int:id>', views.LabExamTestCaseDetail.as_view()),
    path('labexams/answer/<int:id>', views.LabExamAnswerDetail.as_view()),
]