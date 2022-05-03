from rest_framework import serializers

from .models import LabExperiment, LabQuestion, LabTestCase, LabAnswer

from classes.models import Class


class LabTestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestCase
        fields = (
            'id',
            'question',
            'input_file',
            'output_file',
        )


class LabQuestionSerializer(serializers.ModelSerializer):
    testcases = LabTestCaseSerializer(many=True, read_only=True)
    class Meta:
        model = LabQuestion
        fields = (
            'id',
            'question_number',
            'question',
            'language',
            'testcases',
            'answer',
            'mark',
        )


class LabExperimentSerializer(serializers.ModelSerializer):
    questions = LabQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = LabExperiment
        fields = (
            'id',
            'exp_name',
            'created',
            'modified',
            'due_date',
            'total_marks',
            'questions',
        )