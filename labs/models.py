from django.db import models


class LabExperiment(models.Model):
    exp_name = models.CharField(max_length=50)
    class_a = models.ForeignKey('classes.Class', related_name='lab_exps', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()
    total_marks = models.IntegerField()

    def __str__(self):
        return self.class_a.subject.sub_name + ' - ' + self.exp_name


class LabQuestion(models.Model):
    experiment = models.ForeignKey('LabExperiment', related_name='questions', on_delete=models.CASCADE)
    question_number = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    question = models.TextField(max_length=500, blank=True)
    language = models.ForeignKey('editor.Language', on_delete=models.PROTECT)
    answer = models.FileField(upload_to='uploads/lab/correctanswer', blank=True, null=True)
    mark = models.IntegerField()
    # analysis
    # stdExecTime = models.IntegerField(default=5)


    def __str__(self):
        return self.experiment.exp_name + ' - ' + self.title


class LabTestCase(models.Model):
    question = models.ForeignKey('LabQuestion', related_name='testcases', on_delete=models.CASCADE)
    tc_number = models.PositiveIntegerField()
    hidden = models.BooleanField(default=False)
    input_file = models.FileField(upload_to='uploads/lab/testcase/input')
    output_file = models.FileField(upload_to='uploads/lab/testcase/output')
    mark = models.IntegerField()


class LabAnswer(models.Model):
    question = models.ForeignKey('LabQuestion', related_name='answers', on_delete=models.CASCADE)
    student = models.ForeignKey('user.Student', on_delete=models.CASCADE)
    answer = models.FileField(upload_to='uploads/lab/studentanswer')
    submitted = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    execution_tries = models.IntegerField()
    execution_time = models.IntegerField()
    total_marks = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['question', 'student'], name='unique_lab_answer')
        ]