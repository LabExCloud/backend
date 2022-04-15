from django.db import models


class LabExperiments(models.Model):
    exp_name = models.CharField(max_length=50)
    subject = models.ForeignKey('base.Subject', on_delete=models.CASCADE)


class LabQuestions(models.Model):
    experiment = models.ForeignKey('LabExperiment', on_delete=models.CASCADE)
    question_number = models.IntegerField()
    question = models.TextField(max_length=500, blank=True, null=True)
    answer = models.TextField(max_length=500, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()


class LabAnswers(models.Model):
    question = models.ForeignKey('LabQuestions', on_delete=models.CASCADE)
    student = models.ForeignKey('base.Student', on_delete=models.CASCADE)
    answer = models.TextField(max_length=500, blank=True, null=True)
    submitted = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    execution_tries = models.IntegerField()
    execution_time = models.IntegerField()