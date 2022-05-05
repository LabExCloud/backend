from django.contrib import admin

from .models import Language, Question


admin.site.register(Language)
admin.site.register(Question)