from django.urls import path, include

from . import views

urlpatterns = [
    path('labs', views.LabsList.as_view()),
    path('labs/sem', views.LabsSemList.as_view()),
    path('labs/sem/<int:sem>', views.LabsSemList.as_view()),
    path('labs/<int:id>', views.LabExperimentsList.as_view()), 
    path('labs/exp/<int:id>', views.LabExperimentDetail.as_view()),
    path('labs/question/<int:id>', views.LabQuestionDetail.as_view()),
    path('labs/question', views.LabQuestionDetail.as_view()),
    path('labs/testcase/<int:id>', views.LabTestCaseDetail.as_view()),
    path('labs/answer/<int:id>', views.LabAnswerDetail.as_view()),
    path('labs/answer/question/<int:id>', views.LabAnswerStudentQuestion.as_view()),
    path('labs/answers/<int:id>', views.LabAnswersList.as_view()),
]