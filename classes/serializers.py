from rest_framework import serializers

from user.models import User, Teacher
from user.serializers import LightUserSerializer

from .models import Class

from base.models import Subject, Department, Semester, Batch


class ClassSerializer(serializers.ModelSerializer):
    teachers = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Class
        fields = (
            'id',
            'department',
            'semester',
            'subject',
            'batch',
            'owner',
            'teachers',
            'is_lab',
        )
        depth = 1
    
    def get_owner(self, obj):
        serializer = LightUserSerializer(obj.owner.user)
        return serializer.data
    
    def get_teachers(self, obj):
        teachers = [i.user for i in obj.teachers.all()]
        serializer = LightUserSerializer(teachers, many=True)
        return serializer.data