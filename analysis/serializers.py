from rest_framework import serializers


class ExperimentReport:
    def __init__(self, exp, completed, submited_ontime):
        self.exp_name = exp.exp_name
        self.exp_id = exp.id
        self.total_questions = len(exp.questions.all())
        self.completed = completed
        self.submited_ontime = submited_ontime


class ExperimentReportSerializer(serializers.Serializer):
    exp_name = serializers.CharField(max_length=50)
    exp_id = serializers.IntegerField()
    total_questions = serializers.IntegerField()
    completed = serializers.IntegerField()
    submited_ontime = serializers.IntegerField()