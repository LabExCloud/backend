from rest_framework import serializers

from user.models import User, Teacher
from user.serializers import LightUserSerializer

from .models import Class


class ClassSerializer(serializers.ModelSerializer):
    teachers = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Class
        fields = (
            'department',
            'semester',
            'subject',
            'batch',
            'owner',
            'teachers',
        )
        depth = 2
    
    def get_owner(self, obj):
        serializer = LightUserSerializer(obj.owner.user)
        return serializer.data
    
    def get_teachers(self, obj):
        teachers = []
        for i in obj.teachers.all():
            teachers.append(User.objects.get(pk=i.user.id))
        serializer = LightUserSerializer(teachers, many=True)
        return serializer.data