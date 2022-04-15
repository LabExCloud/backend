from rest_framework import serializers

from .models import Resource, ResourceFile

from base.models import Subject


class ResourceFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceFile
        fields = (
            'id',
            'file',
        )

class ResourceSerializer(serializers.ModelSerializer):
    resourcefiles = serializers.SerializerMethodField()
    class Meta:
        model = Resource
        fields = (
            'res_name',
            'created',
            'modified',
            'resourcefiles'
        )
        depth = 1
    
    def get_resourcefiles(self, obj):
        serializer = ResourceFileSerializer(ResourceFile.objects.filter(resource=obj), many=True)
        return serializer.data

class SubjectResourceSerializer(serializers.ModelSerializer):
    resources = serializers.SerializerMethodField()
    class Meta:
        model = Subject
        fields = (
            'subject',
            'resources',
        )
        depth = 3
    
    def get_resources(self, obj):
        serializer = ResourceSerializer(Resource.objects.filter(subject=obj), many=True)
        return serializer.data