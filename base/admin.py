from django.contrib import admin
from .models import Department, Semester, Subject, Class, Batch


admin.site.register(Department)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Batch)
admin.site.register(Class)