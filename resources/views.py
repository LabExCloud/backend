from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from .serializers import ClassResourceSerializer, ResourceSerializer, ResourceDetailSerializer, ResourceFileSerializer
from .models import Resource

from classes.permissions import HasPermission
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


class ModifyResource(APIView):
    permission_classes = [IsAuthenticated & HasPermission]
    
    def post(self, request, id):
        try:
            c = Class.objects.get(pk=id)
            self.check_object_permissions(request, c)
            serializer = ResourceSerializer(data=request.data)
            if(serializer.is_valid()):
                r = serializer.save(class_a=c)
                return Response(ResourceSerializer(r).data)
            return Response('invalid data')
        except(Class.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            r = Resource.objects.get(pk=id)
            self.check_object_permissions(request, r.class_a)
            serializer = ResourceSerializer(r, data=request.data)
            if(serializer.is_valid()):
                r = serializer.save()
                return Response(ResourceSerializer(r).data)
            return Response('invalid data')
        except(Resource.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            r = Resource.objects.get(pk=id)
            self.check_object_permissions(request, r.class_a)
            r.delete()
            return Response('deleted')
        except(Resource.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)


class ModifyResourceFile(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    permission_classes = [IsAuthenticated & HasPermission]

    def post(self, request, id):
        try:
            res = Resource.objects.get(pk=id)
            self.check_object_permissions(request, res.class_a)
            serializer = ResourceFileSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(resource=res)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response('invalid data', status=status.HTTP_400_BAD_REQUEST)
        except(Resource.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        try:
            res_file = ResourceFile.objects.get(pk=id)
            self.check_object_permissions(request, res_file.resource.class_a)
            serializer = ResourceFileSerializer(res_file, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response('invalid data', status=status.HTTP_400_BAD_REQUEST)
        except(ResourceFile.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):
        try:
            res_file = ResourceFile.objects.get(pk=id)
            self.check_object_permissions(request, res_file.resource.class_a)
            res_file.delete()
            return Response('deleted', status=status.HTTP_200_OK)
        except(ResourceFile.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)