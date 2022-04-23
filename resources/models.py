from django.db import models

import os

from base.models import Class

class Resource(models.Model):
    class_a = models.ForeignKey(Class, on_delete=models.CASCADE)
    res_name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject.subject + ' - ' + self.res_name


class ResourceFile(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/resources', )

    def filename(self):
        return os.path.basename(self.file.name)
    
    def __str__(self):
        return self.filename()
    
    def url(self):
        return 'http://127.0.0.1:8000' + self.file.url