from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from .serializers import LabExperimentSerializer, LabQuestionSerializer
from .models import LabExperiment, LabQuestion, LabAnswer

from classes.serializers import ClassSerializer
from classes.permissions import HasPermission
from classes.models import Class


class LabsList(APIView):
    permission_classes = [IsAuthenticated & HasPermission]

    def get(self, request):
        sem = request.user.student.semester
        classes = request.user.student.classes.filter(semester=sem, is_lab=True)
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)


class LabsSemList(APIView):
    permission_classes = [IsAuthenticated & HasPermission]

    def get(self, request, sem, format=None):
        classes = request.user.student.classes.filter(semester=sem, is_lab=True)
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)


class LabExperimentsList(APIView):
    permission_classes = [IsAuthenticated & HasPermission]
    
    def get(self, request, id, format=None):
        lab_exps = LabExperiment.objects.filter(class_a=id)
        serializer = LabExperimentSerializer(lab_exps, many=True)
        return Response(serializer.data)


class LabExperimentDetail(APIView):
    permission_classes = [IsAuthenticated & HasPermission]

    def get(self, request, id, format=None):
        exp = LabExperiment.objects.get(pk=id)
        serializer = LabExperimentSerializer(exp)
        return Response(serializer.data)


class LabQuestionDetail(APIView):
    permission_classes = [IsAuthenticated & HasPermission]

    def get(self, request, id, format=None):
        q = LabQuestion.objects.get(pk=id)
        serializer = LabQuestionSerializer(q)
        return Response(serializer.data)

