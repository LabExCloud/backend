from django.contrib import admin

from .models import LabExperiment, LabQuestion, LabAnswer

admin.site.register(LabExperiment)
admin.site.register(LabQuestion)
admin.site.register(LabAnswer)