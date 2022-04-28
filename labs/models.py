from django.db import models


class LabExperiment(models.Model):
    exp_name = models.CharField(max_length=50)
    class_a = models.ForeignKey('classes.Class', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()


class LabQuestion(models.Model):
    experiment = models.ForeignKey('LabExperiment', on_delete=models.CASCADE)
    question_number = models.IntegerField()
    question = models.TextField(max_length=500, blank=True, null=True)
    # implement testcases 
    # answer = models.FileField(upload_to='uploads/lab/questions', )


class LabAnswer(models.Model):
    question = models.ForeignKey('LabQuestions', on_delete=models.CASCADE)
    student = models.ForeignKey('base.Student', on_delete=models.CASCADE)
    # answer = models.TextField(max_length=500, blank=True, null=True)
    submitted = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    execution_tries = models.IntegerField()
    execution_time = models.IntegerField()