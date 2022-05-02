from rest_framework import serializers

from .models import LabExperiment, LabQuestion, LabTestCase, LabAnswer

from classes.models import Class


class LabExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabExperiment
        fields = (
            'id',
            'exp_name',
            'class_a',
            'created',
            'modified',
            'due_date',
            'total_marks',
        )


class ClassLabSerializer(serializers.ModelSerializer):
    sub_name = serializers.SerializerMethodField()
    sem = serializers.SerializerMethodField()

    class Meta:
        model = Class
        fields = (
            'id',
            'sub_name',
            'sem',
            'owner',
            'teachers',
        )
        depth = 1
    
    def get_sub_name(self, obj):
        return obj.subject.sub_name
    
    def get_sem(self, obj):
        return obj.semester.sem