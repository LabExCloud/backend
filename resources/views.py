from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ResourceSerializer, SubjectResourceSerializer
from .models import Resource

from user.models import User


class ResourceList(APIView):
    def get(self, request, format=None):
        q = request.user.student.semester.subject_set.all()
        # print(q)
        resources = Resource.objects.filter(subject__in=q)
        # print(resources)
        serializer = SubjectResourceSerializer(q, many=True)
        return Response(serializer.data)

    # def get(self, request, format=None):
    #     q = request.user.student.semester.subject_set.all()
    #     print(q)
    #     resources = Resource.objects.filter(subject__in=q)
    #     print(resources)
    #     serializer = ResourceSerializer(resources, many=True)
    #     return Response(serializer.data)