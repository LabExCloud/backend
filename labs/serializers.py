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
            'questions',
        )


class LabQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabQuestion
        fields = (
            'id',
            'experiment',
            'question_number',
            'question',
            'language',
            'testcases',
            # 'answer',
            'mark',
        )


class LabTestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestCase
        fields = (
            'id',
            'question',
            'input_file',
            'output_file',
        )