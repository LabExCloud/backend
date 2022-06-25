from django.urls import path, include

from . import views

urlpatterns = [
    path('analysis/report/<int:cid>/<int:sid>', views.ReportView.as_view()),
    # path('', views..as_view()),
]