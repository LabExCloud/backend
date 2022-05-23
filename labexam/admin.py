from django.contrib import admin

from .models import LabExam, LabExamQuestion, LabExamAnswer, LabExamTestCase

admin.site.register(LabExam)
admin.site.register(LabExamQuestion)
admin.site.register(LabExamAnswer)
admin.site.register(LabExamTestCase)