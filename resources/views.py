from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ClassResourceSerializer


class ResourceList(APIView):
    def get(self, request, format=None):
        sem = request.user.student.semester
        classes = request.user.student.classes.filter(semester=sem)
        serializer = ClassResourceSerializer(classes, many=True)
        return Response(serializer.data)


class ResourceListSem(APIView):
    def get(self, request, sem, format=None):
        classes = request.user.student.classes.filter(semester=sem)
        serializer = ClassResourceSerializer(classes, many=True)
        return Response(serializer.data)