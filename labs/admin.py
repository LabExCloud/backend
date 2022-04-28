from django.contrib import admin

from .models import LabExperiments, LabQuestions, LabAnswers

admin.site.register(LabExperiments)
admin.site.register(LabQuestions)
admin.site.register(LabAnswers)