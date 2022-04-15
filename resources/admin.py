from django.contrib import admin

from .models import Resource, ResourceFile


# reverse lookup
# class ResourceFileInline(admin.TabularInline):
#     model = ResourceFile


# class ResourceAdmin(admin.ModelAdmin):
#     inlines = [
#         ResourceFileInline,
#     ]

admin.site.register(Resource)
admin.site.register(ResourceFile)