from rest_framework import serializers

from .models import LabExperiment, LabQuestion, LabTestCase, LabAnswer

from classes.models import Class


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

    class Meta:
        model = LabExperiment
        exclude = (
            'class_a',
        )


class LabAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabAnswer
        fields = '__all__'