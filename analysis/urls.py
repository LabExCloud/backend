from django.urls import path, include

from . import views

urlpatterns = [
    path('analysis/report/<int:class_id>/<int:student_id>', views.ReportView.as_view()),
    # path('', views..as_view()),
]