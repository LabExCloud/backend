from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from labs.models import LabQuestion, LabAnswer
from classes.models import Class

# Create your views here.


class ReportView(APIView):
    def get(self, request, class_id, student_id):
        t = LabAnswer.objects.filter(student__id=student_id)
        answers = []
        for i in t:
            if i.question.experiment.class_a.id == class_id:
                answers.append(i)

        print(answers)
        return Response(status.HTTP_200_OK)