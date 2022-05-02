from rest_framework import serializers

from .models import Resource, ResourceFile

from classes.models import Class


class ResourceFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceFile
        fields = (
            'id',
            'file',
            'filename',
        )
    
    def create(self, data):
        return ResourceFile.objects.create(**data)
    
    def update(self, instance, data):
        instance.resource = data.get('resource', instance.resource)
        instance.file = data.get('file', instance.file)
        instance.save()
        return instance

class ResourceDetailSerializer(serializers.ModelSerializer):
    res_files = serializers.SerializerMethodField()

    class Meta:
        model = Resource
        fields = (
            'id',
            'res_name',
            'description',
            'created',
            'modified',
            'res_files',
        )
    
    def get_res_files(self, obj):
        serializer = ResourceFileSerializer(obj.res_files.all(), many=True)
        return serializer.data


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = (
            'id',
            'res_name',
            'description',
            'created',
            'modified',
        )
    
    def create(self, data):
        return Resource.objects.create(**data)
    
    def update(self, instance, data):
        instance.res_name = data.get('res_name', instance.res_name)
        instance.description = data.get('description', instance.description)
        instance.save()
        return instance


class ClassResourceSerializer(serializers.ModelSerializer):
    resources = serializers.SerializerMethodField()
    sub_name = serializers.SerializerMethodField()
    sub_code = serializers.SerializerMethodField()
    sem = serializers.SerializerMethodField()

    class Meta:
        model = Class
        fields = (
            'id',
            'sub_name',
            'sub_code',
            'sem',
            'resources',
        )
    
    def get_resources(self, obj):
        serializer = ResourceSerializer(obj.resources, many=True)
        return serializer.data
    
    def get_sub_name(self, obj):
        return obj.subject.sub_name
    
    def get_sub_code(self, obj):
        return obj.subject.sub_code
    
    def get_sem(self, obj):
        return obj.semester.sem