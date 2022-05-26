from rest_framework import serializers

from .models import LabExperiment, LabQuestion, LabTestCase, LabAnswer

from classes.models import Class

from user.serializers import LightUserSerializer


class LabTestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestCase
        exclude = (
            'question',
        )


class LabQuestionSerializer(serializers.ModelSerializer):
    testcases = LabTestCaseSerializer(many=True, read_only=True)
    class Meta:
        model = LabQuestion
        exclude = (
            'experiment',
        )


class LabExperimentSerializer(serializers.ModelSerializer):
    questions = LabQuestionSerializer(many=True, read_only=True)
    subject = serializers.SerializerMethodField()

    class Meta:
        model = LabExperiment
        exclude = (
            'class_a',
        )
    
    def get_subject(self, obj):
        return obj.class_a.subject.sub_name


class LabAnswerSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()
    class Meta:
        model = LabAnswer
        fields = '__all__'

    def get_student(self, obj):
        serializer = LightUserSerializer(obj.student.user)
        return serializer.data