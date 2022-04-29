from django.db import models


class LabExam(models.Model):
    exam_name = models.CharField(max_length=50)
    class_a = models.ForeignKey('classes.Class', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    total_marks = models.IntegerField()


class LabExamQuestion(models.Model):
    exam = models.ForeignKey('LabExam', on_delete=models.CASCADE)
    question_number = models.IntegerField()
    question = models.TextField(max_length=500, blank=True)
    language = models.ForeignKey('editor.Language', on_delete=models.PROTECT)
    # implement testcases 
    # answer = models.FileField(upload_to='uploads/lab/questions', )
    mark = models.IntegerField()


class LabExamAnswer(models.Model):
    question = models.ForeignKey('LabExamQuestions', on_delete=models.CASCADE)
    student = models.ForeignKey('base.Student', on_delete=models.CASCADE)
    # answer = models.TextField(max_length=500, blank=True, null=True)
    submitted = models.DateTimeField(auto_now_add=True)
    
    execution_tries = models.IntegerField()
    execution_time = models.IntegerField()
    total_marks = models.IntegerField()