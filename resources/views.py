from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ClassResourceSerializer, ResourceSerializer, ResourceDetailSerializer
from .models import Resource

from classes.models import Class


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


class ResourceDetail(APIView):
    def get(self, request, r_id, format=None):
        resource = Resource.objects.get(pk=r_id)
        serializer = ResourceDetailSerializer(resource)
        return Response(serializer.data)


# TODO: Implement user check
class ModifyResource(APIView):
    def get(self, request, id):
        return Response('get')
    
    def post(self, request, id):
        try:
            c = Class.objects.get(pk=id)
            serializer = ResourceSerializer(data=request.data)
            serializer.is_valid()
            r = serializer.save(class_a=c)
            return Response(ResourceSerializer(r).data)
        except(Class.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            r = Resource.objects.get(pk=id)
            serializer = ResourceSerializer(r, data=request.data)
            serializer.is_valid()
            r = serializer.save()
            return Response(ResourceSerializer(r).data)
        except(Resource.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            Resource.objects.get(pk=id).delete()
            return Response('deleted')
        except(Resource.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)