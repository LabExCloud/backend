from rest_framework import serializers

from user.serializers import LightUserSerializer

from .models import LabExam, LabExamAnswer, LabExamQuestion, LabExamTestCase


class LabExamTestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabExamTestCase
        exclude = (
            'question',
        )


class LabExamQuestionSerializer(serializers.ModelSerializer):
    testcases = LabExamTestCaseSerializer(many=True, read_only=True)
    class Meta:
        model = LabExamQuestion
        exclude = (
            'exam',
        )


class LabExamSerializer(serializers.ModelSerializer):
    questions = LabExamQuestionSerializer(many=True, read_only=True)
    subject = serializers.SerializerMethodField()

    class Meta:
        model = LabExam
        exclude = (
            'class_a',
        )
    
    def get_subject(self, obj):
        return obj.class_a.subject.sub_name


class LabExamAnswerSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()
    class Meta:
        model = LabExamAnswer
        fields = '__all__'

    def get_student(self, obj):
        serializer = LightUserSerializer(obj.student.user)
        return serializer.data