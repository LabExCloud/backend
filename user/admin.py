from django.contrib import admin

from user.models import Student, Teacher

admin.site.register(Student)
admin.site.register(Teacher)