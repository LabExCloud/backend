from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from .serializers import ClassLabSerializer, LabExperimentSerializer
from .models import LabExperiment, LabQuestion, LabTestCase, LabAnswer

from classes.serializers import ClassSerializer
from classes.permissions import HasPermission
from classes.models import Class


class LabExperimentList(APIView):
    def get(self, request):
        sem = request.user.student.semester
        classes = request.user.student.classes.filter(semester=sem, is_lab=True)
        serializer = ClassLabSerializer(classes, many=True)
        return Response(serializer.data)


class LabExperimentListSem(APIView):
    def get(self, request, sem, format=None):
        classes = request.user.student.classes.filter(semester=sem, is_lab=True)
        serializer = ClassLabSerializer(classes, many=True)
        return Response(serializer.data)