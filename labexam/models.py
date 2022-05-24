from django.db import models


class LabExam(models.Model):
    exam_name = models.CharField(max_length=50)
    class_a = models.ForeignKey('classes.Class', related_name='lab_exams', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    total_marks = models.IntegerField()

    def __str__(self):
        return self.class_a.subject.sub_name + ' - ' + self.exam_name


class LabExamQuestion(models.Model):
    exam = models.ForeignKey('LabExam', related_name='questions', on_delete=models.CASCADE)
    question_number = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    question = models.TextField(max_length=500, blank=True)
    language = models.ForeignKey('editor.Language', on_delete=models.PROTECT)
    answer = models.FileField(upload_to='uploads/labexam/correctanswer', blank=True, null=True)
    mark = models.IntegerField()

    def __str__(self):
        return self.exam.exam_name + ' - ' + self.title


class LabExamTestCase(models.Model):
    question = models.ForeignKey('LabExamQuestion', related_name='testcases', on_delete=models.CASCADE)
    tc_number = models.PositiveIntegerField()
    hidden = models.BooleanField(default=False)
    input_file = models.FileField(upload_to='uploads/labexam/testcase/input')
    output_file = models.FileField(upload_to='uploads/labexam/testcase/output')
    mark = models.IntegerField()


class LabExamAnswer(models.Model):
    question = models.ForeignKey('LabExamQuestion', related_name='answers', on_delete=models.CASCADE)
    student = models.ForeignKey('user.Student', on_delete=models.CASCADE)
    answer = models.FileField(upload_to='uploads/labexam/studentanswer')
    submitted = models.DateTimeField(auto_now_add=True)
    
    execution_tries = models.IntegerField()
    execution_time = models.IntegerField()
    total_marks = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['question', 'student'], name='unique_labexam_answer')
        ]

