from rest_framework import serializers

from .models import Resource, ResourceFile

from base.models import Subject


class ResourceFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceFile
        fields = (
            'id',
            'url',
            'filename',
        )

class ResourceSerializer(serializers.ModelSerializer):
    resource_files = serializers.SerializerMethodField()
    class Meta:
        model = Resource
        fields = (
            'id',
            'res_name',
            'created',
            'modified',
            'resource_files'
        )
        depth = 1
    
    def get_resource_files(self, obj):
        serializer = ResourceFileSerializer(ResourceFile.objects.filter(resource=obj), many=True)
        return serializer.data

class SubjectResourceSerializer(serializers.ModelSerializer):
    resources = serializers.SerializerMethodField()
    class Meta:
        model = Subject
        fields = (
            'id',
            'subject',
            'resources',
        )
        depth = 3
    
    def get_resources(self, obj):
        serializer = ResourceSerializer(Resource.objects.filter(subject=obj), many=True)
        return serializer.data