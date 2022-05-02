from django.contrib import admin

from .models import LabExperiment, LabQuestion, LabAnswer, LabTestCase

admin.site.register(LabExperiment)
admin.site.register(LabQuestion)
admin.site.register(LabTestCase)
admin.site.register(LabAnswer)