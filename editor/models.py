from django.db import models

class Language(models.Model):
    language = models.CharField(max_length=10, unique=True)
    piston_lang = models.CharField(max_length=10, unique=True)
    editor_lang = models.CharField(max_length=10, unique=True)
    demo_code = models.TextField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['language', 'piston_lang', 'editor_lang'], name='unique_lang')
        ]

    def __str__(self):
        return self.language


class Question(models.Model):
    question_number = models.IntegerField()
    question = models.TextField(max_length=500, blank=True)
    language = models.ForeignKey('Language', on_delete=models.PROTECT)
    answer = models.FileField(upload_to='uploads/editor/correctanswer', blank=True, null=True)
    mark = models.IntegerField()
    fullscreen = models.BooleanField(default=False)


class TestCase(models.Model):
    question = models.ForeignKey('Question', related_name='testcases', on_delete=models.CASCADE)
    hidden = models.BooleanField(default=False)
    input_file = models.FileField(upload_to='uploads/editor/testcase/input')
    output_file = models.FileField(upload_to='uploads/editor/testcase/output')
    mark = models.IntegerField()
